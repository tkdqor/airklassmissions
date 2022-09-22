from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """
    Assignee : 상백

    has_permission : 로그인이 된 유저 중 is_master 필드가 True인 강사만 접근 가능
    hasattr로 로그인이 된 유저가 master 객체와 관계가 있는지 확인
    일반 유저가 접근 시 에러 발생
    """

    def has_permission(self, request, view):
        if hasattr(request.user, "user_master"):
            return request.user.is_authenticated
        else:
            return False
