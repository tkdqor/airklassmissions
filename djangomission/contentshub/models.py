from django.db import models


class Master(models.Model):
    """
    Assignee : 상백

    Master 모델은 Klass 모델 및 Answer 모델과 1:N 관계로 설정되어 있습니다.
    그리고 User 모델과 1:1 관계로 설정되어 있습니다.
    강사의 이름과 이메일 정보와 함께 에어클래스의 강사로 등록합니다.
    """

    user = models.OneToOneField(
        to="accounts.User", verbose_name="유저", on_delete=models.CASCADE, related_name="user_master"
    )
    username = models.CharField("이름", max_length=20)
    email = models.EmailField("이메일", max_length=100, unique=True)
    created_at = models.DateTimeField("등록일", auto_now_add=True)
    updated_at = models.DateTimeField("수정일", auto_now=True)


class Klass(models.Model):
    """
    Assignee : 상백

    Master 모델과 1:N 관계를 가지는 Klass 모델입니다.
    강의의 제목과 요약 내용을 기록할 수 있습니다.
    """

    master = models.ForeignKey(to="Master", verbose_name="강사", on_delete=models.CASCADE, related_name="master_klass")
    title = models.CharField("제목", max_length=50)
    summary = models.CharField("요약", max_length=100)
    created_at = models.DateTimeField("생성일", auto_now_add=True)
    updated_at = models.DateTimeField("수정일", auto_now=True)
