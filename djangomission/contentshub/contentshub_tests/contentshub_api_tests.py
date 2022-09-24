from rest_framework.test import APIClient, APITestCase

from accounts.models import User


class KlassCreateAPIViewPassTestCase(APITestCase):
    """
    Assignee : 상백

    로그인된 강사의 강의 생성 확인 테스트입니다.
    setUp 메서드로 강사 객체를 생성합니다.
    해당 API로 POST 요청을 했을 때, 강의 데이터가 생성 되어 status code 201을 응답하는 것을 확인합니다.
    """

    url = "/api/v1/klasses"

    def setUp(self):
        """강사 객체 생성 설정"""
        self.user = User.objects.create(email="aaa@naver.com", password="1234", is_master=True)
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_klass(self):
        """Klass 객체 생성 테스트"""
        klass_data = {"title": "칼퇴요정의 남다른 엑셀 비법", "summary": "EXCEL의 기초부터 심화까지 낱낱이 알아 보자"}
        response = self.client.post(self.url, data=klass_data, format="json")
        self.assertEqual(response.status_code, 201)


class KlassCreateAPIViewFailTestCase(APITestCase):
    """
    Assignee : 상백

    로그인된 유저의 강의 생성 확인 테스트입니다.
    setUp 메서드로 유저 객체를 생성합니다.
    해당 API로 POST 요청을 했을 때, 강의 데이터가 생성 되지않아 permission_classes로부터 status code 403을 응답하는 것을 확인합니다.
    """

    url = "/api/v1/klasses"

    def setUp(self):
        """유저 객체 생성 설정"""
        self.user = User.objects.create(email="aaa@naver.com", password="1234", is_master=False)
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_klass(self):
        """Klass 객체 생성 테스트"""
        klass_data = {"title": "칼퇴요정의 남다른 엑셀 비법", "summary": "EXCEL의 기초부터 심화까지 낱낱이 알아 보자"}
        response = self.client.post(self.url, data=klass_data, format="json")
        self.assertEqual(response.status_code, 403)
