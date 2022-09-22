from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from contentshub.models import Klass

from .models import Question
from .serializers import QuestionModelSerializer


# url : POST /api/v1/klasses/<klass_id>
class QuestionCreateAPIView(APIView):
    """
    Assignee : 상백

    permission = 서비스에 로그인한 모든 유저가 요청 가능
    Http method = POST
    POST : 특정 강의에 속하는 질문 생성
    """

    permission_classes = [IsAuthenticated]

    def post(self, request, klass_id):
        """
        Assignee : 상백

        클라이언트의 요청 및 JSON 형태 데이터 입력 시, 특정 강의에 속하는 질문 데이터를 생성하는 메서드입니다.
        ex) {"contents": "기타를 연습하다 보니 손이 너무 아픈데 어떻게 해야 할까요?"}
        또한, 특정 강의의 id값을 path 파라미터로 입력해야 합니다.
        그리고 context 딕셔너리로 로그인된 유저 객체 및 강의 객체를 보내서 클라이언트가 따로 입력하지 않게 설정했습니다.
        """

        try:
            klass = Klass.objects.get(id=klass_id)
            context = {"user": request.user, "klass": klass}
            serializer = QuestionModelSerializer(data=request.data, context=context)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Klass.DoesNotExist:
            return Response({"error": "해당 klass_id로 존재하는 강의가 없습니다. 다시 한 번 확인해주세요!"}, status=status.HTTP_404_NOT_FOUND)


# url : PATCH /api/v1/questions/<question_id>
class QuestionDeleteAPIView(APIView):
    """
    Assignee : 상백

    permission = 서비스에 로그인한 모든 유저가 요청 가능
    Http method = PATCH
    PATCH : 유저가 생성한 질문 삭제 및 복구
    """

    permission_classes = [IsAuthenticated]

    def patch(self, request, question_id):
        """
        Assignee : 상백

        로그인한 유저가 생성한 질문을 삭제하기 위한 메서드입니다. 특정 질문의 id값을 path 파라미터로 입력해야 합니다.
        question_id로 존재하는 객체가 없다면 에러 메시지를 응답합니다.
        is_deleted 필드를 true로 설정 후 JSON 형태로 요청하면 삭제 처리가 되고, false로 설정 후 JSON 형태로 요청하면 복구가 됩니다.
        ex) {"is_deleted": true} 또는 {"is_deleted": false}
        """

        if request.data.get("contents", None):
            return Response({"error": "변경할 수 없는 정보입니다. is_deleted만 수정이 가능합니다."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            question = Question.objects.get(id=question_id, user=request.user)
            if request.data["is_deleted"] == True:
                question.is_deleted = True
                question.save()
                return Response({"message": "해당 질문을 삭제했습니다!"}, status=status.HTTP_200_OK)
            elif request.data["is_deleted"] == False:
                question.is_deleted = False
                question.save()
                return Response({"message": "해당 질문을 복구했습니다!"}, status=status.HTTP_200_OK)
        except Question.DoesNotExist:
            return Response(
                {"error": "해당 question_id로 존재하는 질문이 없습니다. 다시 한 번 확인해주세요!"}, status=status.HTTP_404_NOT_FOUND
            )
