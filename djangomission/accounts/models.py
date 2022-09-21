from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from contentshub.models import Master


class CustomUserManager(BaseUserManager):
    """
    Assignee : 상백

    custom user model를 사용하기 위해 BaseUserManager 클래스와 create_user, create_superuser 함수를 정의합니다.
    email로 회원가입을 하기 위해 create_user 함수에 ValueError를 설정합니다.
    """

    def create_user(self, email, password):
        if not email:
            raise ValueError("회원가입 시, 이메일이 필요합니다.")
        user = self.model(
            email=email,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """python manage.py createsuperuser 사용 시 해당 함수가 사용됩니다."""
        user = self.create_user(
            email=email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    """
    Assignee : 상백

    AbstractBaseUser 클래스를 상속받아 User 모델을 정의합니다.
    id를 PK로 설정하고 로그인 시 email 필드가 사용되도록 설정합니다.
    is_master 필드를 생성하여 회원가입 시, 수강생으로 가입을 하는 경우에는 False / 강사로 가입을 하는 경우에는 True로 설정합니다.
    django Signal를 사용해서 is_master 필드값이 True인 경우, 자동으로 Master 모델 객체를 생성해줍니다.
    """

    id = models.BigAutoField(primary_key=True)
    username = models.CharField("이름", max_length=20)
    email = models.EmailField("이메일", max_length=100, unique=True)
    password = models.CharField("비밀번호", max_length=128)
    is_master = models.BooleanField("강사여부", default=False)

    """is_active가 False일 경우 계정이 비활성화됨"""
    is_active = models.BooleanField("활성화", default=True)

    """is_staff에서 해당 값 사용"""
    is_admin = models.BooleanField("관리자", default=False)

    created_at = models.DateTimeField("가입일", auto_now_add=True)
    updated_at = models.DateTimeField("수정일", auto_now=True)

    """"
    # id로 사용할 필드 지정.
    # 로그인 시 USERNAME_FIELD에 설정 된 필드와 password가 사용됩니다.
    """
    USERNAME_FIELD = "email"

    """user를 생성할 때 입력받을 필드 지정"""
    REQUIRED_FIELDS = []

    """custom user 생성 시 필요"""
    objects = CustomUserManager()

    def __str__(self):
        return f"email: {self.email} / name: {self.username}"

    def has_perm(self, perm, obj=None):
        """
        # 로그인 사용자의 특정 테이블의 crud 권한을 설정, perm table의 crud 권한이 들어간다.
        # admin일 경우 항상 True, 비활성 사용자(is_active=False)의 경우 항상 False
        """
        return True

    def has_module_perms(self, app_label):
        """ "
        # 로그인 사용자의 특정 app에 접근 가능 여부를 설정, app_label에는 app 이름이 들어간다.
        # admin일 경우 항상 True, 비활성 사용자(is_active=False)의 경우 항상 False
        """
        return True

    @property
    def is_staff(self):
        """admin 권한 설정"""
        return self.is_admin


# django Signal을 이용하여 User 모델 생성 시, is_master 필드값이 True라면 Master 모델 객체 생성
@receiver(post_save, sender=User)
def on_save_user(sender, instance, **kwargs):
    if instance.is_master == True:
        username = instance.username
        email = instance.email
        Master.objects.create(user=instance, username=username, email=email)
