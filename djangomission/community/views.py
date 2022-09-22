from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from contentshub.models import Klass

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
            serializer = QuestionModelSerializer(data=request.data, context=context)  # noqa
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)  # noqa
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # noqa
        except Klass.DoesNotExist:
            return Response(
                {"error": "해당 klass_id로 존재하는 강의가 없습니다. 다시 한 번 확인해주세요!"}, status=status.HTTP_404_NOT_FOUND  # noqa
            )  # noqa
