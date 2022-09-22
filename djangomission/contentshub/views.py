from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from djangomission.permissions import IsOwner

from .serializers import KlassModelSerializer


# url : POST /api/v1/klasses
class KlassCreateAPIView(APIView):
    """
    Assignee : 상백

    permission = 로그인된 강사만 요청 가능
    Http method = POST
    POST : 강의 생성
    """

    permission_classes = [IsOwner]

    def post(self, request):
        """
        Assignee : 상백

        클라이언트의 요청 및 JSON 형태 데이터 입력 시, 강의 데이터를 생성하는 메서드입니다.
        ex) {"title": "악보없이 완주가능한 통기타 초급 강의","summary": "누구나 시작할 수 있는 기타 강의"}
        또한, context 딕셔너리로 로그인된 강사 객체를 보내주어 클라이언트가 강사 id를 입력하지 않게 설정했습니다.
        """

        context = {"master": request.user.user_master}
        serializer = KlassModelSerializer(data=request.data, context=context)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
