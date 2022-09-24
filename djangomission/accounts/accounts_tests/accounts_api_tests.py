from rest_framework.test import APIClient, APITestCase

from accounts.models import User


class SignUpViewTestCase(APITestCase):
    """
    Assignee : 상백

    회원가입 테스트입니다.
    회원가입시 필요한 email과 password, username 그리고 is_master를 JSON 형태로 요청할 때 유저가 등록됩니다.
    해당 API로 POST 요청을 했을 때, 회원가입이 진행되어 status code 201을 응답하는 것을 확인합니다.
    """

    url = "/api/v1/users/signup"

    def test_signup(self):
        """회원가입 테스트"""
        user_data = {"email": "aaa@naver.com", "password": "1234", "username": "sangsang", "is_master": True}
        self.client = APIClient()
        response = self.client.post(self.url, data=user_data, format="json")
        self.assertEqual(response.status_code, 201)


class SignInViewTestCase(APITestCase):
    """
    Assignee : 상백

    회원 로그인 테스트입니다.
    로그인할 때 필요한 email과 password를 JSON 형태로 요청할 때 유저가 로그인됩니다.
    해당 API로 POST 요청을 했을 때, 로그인이 진행되어 status code 200을 응답하는 것을 확인합니다.
    또한, email과 password가 각각 다를 때 status code 404를 확인합니다.
    """

    url = "/api/v1/users/signin"

    def setUp(self):
        """유저 생성 설정"""
        self.email = "aaa@naver.com"
        self.password = "1234"
        self.username = "sangsang"
        self.is_master = True
        self.user = User.objects.create_user(self.email, self.password)
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_authentication(self):
        """로그인 테스트"""
        response = self.client.post(self.url, {"email": self.email, "password": self.password})
        self.assertEqual(response.status_code, 200)

    def test_authentication_with_wrong_email(self):
        """email이 다를 때 테스트"""
        response = self.client.post(self.url, {"email": "abc@naver.com", "password": self.password})
        self.assertEqual(response.status_code, 404)

    def test_authentication_with_wrong_password(self):
        """password가 다를 때 테스트"""
        response = self.client.post(self.url, {"email": self.email, "password": "123456"})
        self.assertEqual(response.status_code, 404)
