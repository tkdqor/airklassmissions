from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import SignUpSerializer


# url : POST api/v1/users/signup
class SignUpView(APIView):
    """
    Assignee : 상백

    회원가입을 진행하는 APIView입니다.
    권한은 누구나 접근할 수 있게 설정하고 회원가입 성공 시, 201 code를 응답합니다.
    is_master 필드를 false로 설정 후 JSON 형태로 요청하면 수강생으로 가입이 진행되고, true로 설정 후 요청하면 강사로 가입이 진행됩니다.
    """

    permission_classes = [AllowAny]
    serializer = SignUpSerializer

    def post(self, request):
        serializer = self.serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            res = Response(
                {
                    "message": "회원가입에 성공했습니다.",
                },
                status=status.HTTP_201_CREATED,
            )
            return res
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
