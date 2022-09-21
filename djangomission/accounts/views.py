from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import SignInSerializer, SignUpSerializer, UserTokenObtainPairSerializer


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


# url : POST api/v1/users/signin
class SignInView(APIView):
    """
    Assignee : 상백

    로그인을 진행하는 APIView입니다.
    로그인 성공 시, 클라이언트에게 access token과 refresh token을 리턴합니다.
    로그인에 실패할 경우, 404 code를 응답합니다.
    """

    permission_classes = [AllowAny]
    serializer = SignInSerializer

    def post(self, request):
        user = authenticate(request, email=request.data.get("email"), password=request.data.get("password"))
        if not user:
            return Response({"error": "이메일 또는 비밀번호를 잘못 입력했습니다."}, status=status.HTTP_404_NOT_FOUND)

        login(request, user)

        token = UserTokenObtainPairSerializer.get_token(user)

        res = Response(
            {
                "message": f"{user.email}님, 로그인이 완료되었습니다!",
                "token": {
                    "access": str(token.access_token),
                    "refresh": str(token),
                },
            },
            status=status.HTTP_200_OK,
        )
        return res
