from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()


class UserTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Assignee : 상백

    access token과 refresh token를 발행해주는 시리얼라이저입니다.
    로그인 시, 유저에게 응답해주기 위해 설정합니다.
    """

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token


class SignUpSerializer(serializers.ModelSerializer):
    """
    Assignee : 상백

    User 모델을 위한 회원가입 시리얼라이저입니다.
    회원가입 시, email에 대한 유효성 검사를 진행합니다.
    """

    def create(self, validated_data):
        email = validated_data.get("email")
        password = validated_data.get("password")
        username = validated_data.get("username")
        is_master = validated_data.get("is_master")
        user = User(email=email, password=password, username=username, is_master=is_master)
        user.set_password(password)
        user.save()
        return user

    class Meta:
        model = User
        fields = ("email", "password", "username", "is_master")


class SignInSerializer(serializers.ModelSerializer):
    """
    Assignee : 상백

    User 모델 로그인 시리얼라이저입니다.
    로그인 시, email과 password를 확인합니다.
    """

    class Meta:
        model = User
        fields = ("email", "password")
