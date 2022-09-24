from rest_framework.test import APIClient, APITestCase

from accounts.models import User
from community.models import Answer, Question
from contentshub.models import Klass, Master


class KlassRetrieveAPIViewPassTestCase(APITestCase):
    """
    Assignee : 상백

    서비스에 로그인한 모든 유저가 특정 강의에 작성된 질문과 답변을 확인할 수 있는 테스트입니다.
    setUp 메서드로 유저, 강사, klass, question, answer 객체를 생성합니다.
    해당 API로 GET 요청을 했을 때, 존재하는 klass일 경우 status code 200을 응답하는 것을 확인합니다.
    """

    url = "/api/v1/klasses/1"

    def setUp(self):
        """유저, 강사, klass, question, answer 객체 생성 설정"""
        self.user = User.objects.create(email="aaa@naver.com", password="1234", is_master=False)
        self.user2 = User.objects.create(email="bbb@naver.com", password="1234", is_master=False)
        self.master = Master.objects.create(user_id=self.user2.id, email="bbb@naver.com", username="sangsang")
        self.client = APIClient()
        self.client.force_authenticate(self.user)
        self.klass = Klass.objects.create(
            master_id=self.master.id, title="칼퇴요정의 남다른 엑셀 비법", summary="EXCEL의 기초부터 심화까지 낱낱이 알아 보자"
        )
        self.question = Question.objects.create(
            klass_id=self.klass.id, user_id=self.user.id, contents="엑셀 단축키를 자주 잊어버리는데 어떻게 해야 할까요?"
        )
        self.answer = Answer.objects.create(
            question_id=self.question.id,
            master_id=self.master.id,
            contents="자주 사용되는 엑셀 단축키 정리 파일이 강의자료에 포함되어 있으니 확인해주시면 감사하겠습니다:)",
        )

    def test_klass_retrieve(self):
        """klass 객체 조회 테스트"""
        response = self.client.get(self.url, format="json")
        self.assertEqual(response.status_code, 200)


class KlassRetrieveAPIViewFailTestCase(APITestCase):
    """
    Assignee : 상백

    서비스에 로그인한 모든 유저가 특정 강의에 작성된 질문과 답변을 확인할 수 있는 테스트입니다.
    setUp 메서드로 유저, 강사, klass, question, answer 객체를 생성합니다.
    해당 API로 GET 요청을 했을 때, 존재하지 않는 klass일 경우 status code 404를 응답하는 것을 확인합니다.
    """

    url = "/api/v1/klasses/2"

    def setUp(self):
        """유저, 강사, klass, question, answer 객체 생성 설정"""
        self.user = User.objects.create(email="aaa@naver.com", password="1234", is_master=False)
        self.user2 = User.objects.create(email="bbb@naver.com", password="1234", is_master=False)
        self.master = Master.objects.create(user_id=self.user2.id, email="bbb@naver.com", username="sangsang")
        self.client = APIClient()
        self.client.force_authenticate(self.user)
        self.klass = Klass.objects.create(
            master_id=self.master.id, title="칼퇴요정의 남다른 엑셀 비법", summary="EXCEL의 기초부터 심화까지 낱낱이 알아 보자"
        )
        self.question = Question.objects.create(
            klass_id=self.klass.id, user_id=self.user.id, contents="엑셀 단축키를 자주 잊어버리는데 어떻게 해야 할까요?"
        )
        self.answer = Answer.objects.create(
            question_id=self.question.id,
            master_id=self.master.id,
            contents="자주 사용되는 엑셀 단축키 정리 파일이 강의자료에 포함되어 있으니 확인해주시면 감사하겠습니다:)",
        )

    def test_klass_retrieve(self):
        """klass 객체 조회 테스트"""
        response = self.client.get(self.url, format="json")
        self.assertEqual(response.status_code, 404)


class QuestionCreateAPIViewPassTestCase(APITestCase):
    """
    Assignee : 상백

    서비스에 로그인한 모든 유저가 특정 강의에 속하는 질문을 생성하는 테스트입니다.
    setUp 메서드로 유저, 강사, klass 객체를 생성합니다.
    해당 API로 POST 요청을 했을 때, 존재하는 klass에 속하는 질문이 생성될 경우 status code 201을 응답하는 것을 확인합니다.
    """

    url = "/api/v1/klasses/1/questions"

    def setUp(self):
        """유저, 강사, klass 객체 생성 설정"""
        self.user = User.objects.create(email="aaa@naver.com", password="1234", is_master=False)
        self.user2 = User.objects.create(email="bbb@naver.com", password="1234", is_master=False)
        self.master = Master.objects.create(user_id=self.user2.id, email="bbb@naver.com", username="sangsang")
        self.client = APIClient()
        self.client.force_authenticate(self.user)
        self.klass = Klass.objects.create(
            master_id=self.master.id, title="칼퇴요정의 남다른 엑셀 비법", summary="EXCEL의 기초부터 심화까지 낱낱이 알아 보자"
        )

    def test_question(self):
        """Question 객체 생성 테스트"""
        klass_data = {"contents": "엑셀 단축키를 자주 잊어버리는데 어떻게 해야 할까요?"}
        response = self.client.post(self.url, data=klass_data, format="json")
        self.assertEqual(response.status_code, 201)


class QuestionCreateAPIViewFailTestCase(APITestCase):
    """
    Assignee : 상백

    서비스에 로그인한 모든 유저가 특정 강의에 속하는 질문을 생성하는 테스트입니다.
    setUp 메서드로 유저, 강사, klass 객체를 생성합니다.
    해당 API로 POST 요청을 했을 때, 존재하는 klass에 속하는 질문의 적합하지 않은 필드 데이터를 입력할 경우
    status code 400을 응답하는 것을 확인합니다.
    또한, 해당 API로 POST 요청을 했을 때, 존재하지 않는 klass에 데이터를 입력할 경우 status code 404을 응답하는 것을 확인합니다.
    """

    url = "/api/v1/klasses/1/questions"
    second_url = "/api/v1/klasses/2/questions"

    def setUp(self):
        """유저, 강사, klass 객체 생성 설정"""
        self.user = User.objects.create(email="aaa@naver.com", password="1234", is_master=False)
        self.user2 = User.objects.create(email="bbb@naver.com", password="1234", is_master=False)
        self.master = Master.objects.create(user_id=self.user2.id, email="bbb@naver.com", username="sangsang")
        self.client = APIClient()
        self.client.force_authenticate(self.user)
        self.klass = Klass.objects.create(
            master_id=self.master.id, title="칼퇴요정의 남다른 엑셀 비법", summary="EXCEL의 기초부터 심화까지 낱낱이 알아 보자"
        )

    def test_question_field(self):
        """Question 객체 생성 테스트"""
        klass_data = {"title": "엑셀 단축키를 자주 잊어버리는데 어떻게 해야 할까요?"}
        response = self.client.post(self.url, data=klass_data, format="json")
        self.assertEqual(response.status_code, 400)

    def test_question_DoesNotExist(self):
        """Question 객체 생성 테스트"""
        klass_data = {"contents": "엑셀 단축키를 자주 잊어버리는데 어떻게 해야 할까요?"}
        response = self.client.post(self.second_url, data=klass_data, format="json")
        self.assertEqual(response.status_code, 404)


class QuestionDeleteAPIViewPassTestCase(APITestCase):
    """
    Assignee : 상백

    서비스에 로그인한 유저가 생성한 질문을 삭제 및 복구하는 테스트입니다.
    setUp 메서드로 유저, 강사, klass, question 객체를 생성합니다.
    해당 API로 PATCH 요청을 했을 때, 질문 삭제 및 복구한 경우 status code 200을 응답하는 것을 확인합니다.
    """

    url = "/api/v1/questions/1"

    def setUp(self):
        """유저, 강사, klass, question 객체 생성 설정"""
        self.user = User.objects.create(email="aaa@naver.com", password="1234", is_master=False)
        self.user2 = User.objects.create(email="bbb@naver.com", password="1234", is_master=False)
        self.master = Master.objects.create(user_id=self.user2.id, email="bbb@naver.com", username="sangsang")
        self.client = APIClient()
        self.client.force_authenticate(self.user)
        self.klass = Klass.objects.create(
            master_id=self.master.id, title="칼퇴요정의 남다른 엑셀 비법", summary="EXCEL의 기초부터 심화까지 낱낱이 알아 보자"
        )
        self.question = Question.objects.create(
            klass_id=self.klass.id, user_id=self.user.id, contents="엑셀 단축키를 자주 잊어버리는데 어떻게 해야 할까요?"
        )

    def test_question_delete(self):
        """question 객체 삭제 테스트"""
        question_data = {"is_deleted": True}
        response = self.client.patch(self.url, data=question_data, format="json")
        self.assertEqual(response.status_code, 200)

    def test_question_restore(self):
        """question 객체 복구 테스트"""
        question_data = {"is_deleted": False}
        response = self.client.patch(self.url, data=question_data, format="json")
        self.assertEqual(response.status_code, 200)


class QuestionDeleteAPIViewFailTestCase(APITestCase):
    """
    Assignee : 상백

    서비스에 로그인한 유저가 생성한 질문을 삭제 및 복구하는 테스트입니다.
    setUp 메서드로 유저, 강사, klass, question 객체를 생성합니다.
    해당 API로 PATCH 요청을 했을 때, 변경할 수 없는 필드를 입력한 경우 status code 400을 응답하는 것을 확인합니다.
    또한, 존재하지 않는 질문을 요청할 경우 status code 404을 응답하는 것을 확인합니다.
    """

    url = "/api/v1/questions/1"
    second_url = "/api/v1/questions/2"

    def setUp(self):
        """유저, 강사, klass, question 객체 생성 설정"""
        self.user = User.objects.create(email="aaa@naver.com", password="1234", is_master=False)
        self.user2 = User.objects.create(email="bbb@naver.com", password="1234", is_master=False)
        self.master = Master.objects.create(user_id=self.user2.id, email="bbb@naver.com", username="sangsang")
        self.client = APIClient()
        self.client.force_authenticate(self.user)
        self.klass = Klass.objects.create(
            master_id=self.master.id, title="칼퇴요정의 남다른 엑셀 비법", summary="EXCEL의 기초부터 심화까지 낱낱이 알아 보자"
        )
        self.question = Question.objects.create(
            klass_id=self.klass.id, user_id=self.user.id, contents="엑셀 단축키를 자주 잊어버리는데 어떻게 해야 할까요?"
        )

    def test_question_delete(self):
        """question 객체 필드 데이터 테스트"""
        question_data = {"contents": "엑셀 단축키를 자주 잊어버리는데 어떻게 해야 할까요?"}
        response = self.client.patch(self.url, data=question_data, format="json")
        self.assertEqual(response.status_code, 400)

    def test_question_DoesNotExist(self):
        """Question 객체 삭제 테스트"""
        question_data = {"is_deleted": True}
        response = self.client.patch(self.second_url, data=question_data, format="json")
        self.assertEqual(response.status_code, 404)


class QuestionDeleteAPIViewUserFailTestCase(APITestCase):
    """
    Assignee : 상백

    서비스에 로그인한 유저가 생성한 질문을 삭제하는 테스트입니다.
    setUp 메서드로 유저, 강사, klass, question, answer 객체를 생성합니다.
    해당 API로 PATCH 요청을 했을 때, 답변이 있는 질문을 삭제하려는 경우 status code 400을 응답하는 것을 확인합니다.
    """

    url = "/api/v1/questions/1"

    def setUp(self):
        """유저, 강사, klass, question, answer 객체 생성 설정"""
        self.user = User.objects.create(email="aaa@naver.com", password="1234", is_master=False)
        self.user2 = User.objects.create(email="bbb@naver.com", password="1234", is_master=False)
        self.master = Master.objects.create(user_id=self.user2.id, email="bbb@naver.com", username="sangsang")
        self.client = APIClient()
        self.client.force_authenticate(self.user)
        self.klass = Klass.objects.create(
            master_id=self.master.id, title="칼퇴요정의 남다른 엑셀 비법", summary="EXCEL의 기초부터 심화까지 낱낱이 알아 보자"
        )
        self.question = Question.objects.create(
            klass_id=self.klass.id, user_id=self.user.id, contents="엑셀 단축키를 자주 잊어버리는데 어떻게 해야 할까요?"
        )
        self.answer = Answer.objects.create(
            question_id=self.question.id,
            master_id=self.master.id,
            contents="자주 사용되는 엑셀 단축키 정리 파일이 강의자료에 포함되어 있으니 확인해주시면 감사하겠습니다:)",
        )

    def test_question_delete(self):
        """question 객체 삭제 테스트"""
        question_data = {"is_deleted": True}
        response = self.client.patch(self.url, data=question_data, format="json")
        self.assertEqual(response.status_code, 400)


class QuestionDeleteAPIViewMasterTestCase(APITestCase):
    """
    Assignee : 상백

    서비스에 로그인한 강사가 생성한 질문을 삭제 및 복구하는 테스트입니다.
    setUp 메서드로 강사, klass, question 객체를 생성합니다.
    해당 API로 PATCH 요청을 했을 때, 질문 삭제 및 복구한 경우 status code 200을 응답하는 것을 확인합니다.
    또한, 지금 로그인된 강사의 강의가 아닌 경우 status code 404을 응답하는 것을 확인합니다.
    """

    url = "/api/v1/questions/1"
    second_url = "/api/v1/questions/2"

    def setUp(self):
        """강사, klass, question 객체 생성 설정"""
        self.user = User.objects.create(email="aaa@naver.com", password="1234", is_master=True)
        self.user2 = User.objects.create(email="bbb@naver.com", password="1234", is_master=False)
        self.client = APIClient()
        self.client.force_authenticate(self.user)
        self.klass = Klass.objects.create(
            master_id=self.user.id, title="칼퇴요정의 남다른 엑셀 비법", summary="EXCEL의 기초부터 심화까지 낱낱이 알아 보자"
        )
        self.question = Question.objects.create(
            klass_id=self.klass.id, user_id=self.user2.id, contents="엑셀 단축키를 자주 잊어버리는데 어떻게 해야 할까요?"
        )

    def test_question_delete(self):
        """question 객체 삭제 테스트"""
        question_data = {"is_deleted": True}
        response = self.client.patch(self.url, data=question_data, format="json")
        self.assertEqual(response.status_code, 200)

    def test_question_restore(self):
        """question 객체 복구 테스트"""
        question_data = {"is_deleted": False}
        response = self.client.patch(self.url, data=question_data, format="json")
        self.assertEqual(response.status_code, 200)

    def test_question_delete(self):
        """question 객체 삭제 테스트"""
        question_data = {"is_deleted": True}
        response = self.client.patch(self.second_url, data=question_data, format="json")
        self.assertEqual(response.status_code, 404)


class AnswerCreateAPIViewTestCase(APITestCase):
    """
    Assignee : 상백

    서비스에 로그인한 강사가 생성한 강의에 달린 질문에 답변을 생성하는 테스트입니다.
    setUp 메서드로 유저, 강사, klass, question 객체를 생성합니다.
    해당 API로 POST 요청을 했을 때, 답변이 생성된 경우 status code 201을 응답하는 것을 확인합니다.
    또한, 존재하지 않는 강의의 질문인 경우 status code 404을 응답하는 것을 확인합니다.
    """

    url = "/api/v1/questions/1/answer"
    second_url = "/api/v1/questions/2/answer"

    def setUp(self):
        """유저, 강사, klass, question 객체 생성 설정"""
        self.user = User.objects.create(email="aaa@naver.com", password="1234", is_master=True)
        self.user2 = User.objects.create(email="bbb@naver.com", password="1234", is_master=False)
        self.client = APIClient()
        self.client.force_authenticate(self.user)
        self.klass = Klass.objects.create(
            master_id=self.user.id, title="칼퇴요정의 남다른 엑셀 비법", summary="EXCEL의 기초부터 심화까지 낱낱이 알아 보자"
        )
        self.question = Question.objects.create(
            klass_id=self.klass.id, user_id=self.user2.id, contents="엑셀 단축키를 자주 잊어버리는데 어떻게 해야 할까요?"
        )

    def test_answer(self):
        """answer 객체 생성 테스트"""
        answer_data = {"contents": "자주 사용되는 엑셀 단축키 정리 파일이 강의자료에 포함되어 있으니 확인해주시면 감사하겠습니다:)"}
        response = self.client.post(self.url, data=answer_data, format="json")
        self.assertEqual(response.status_code, 201)

    def test_answer_DoesNotExist(self):
        """answer 객체 생성 테스트"""
        answer_data = {"contents": "자주 사용되는 엑셀 단축키 정리 파일이 강의자료에 포함되어 있으니 확인해주시면 감사하겠습니다:)"}
        response = self.client.post(self.second_url, data=answer_data, format="json")
        self.assertEqual(response.status_code, 404)
