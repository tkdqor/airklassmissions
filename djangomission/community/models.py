from django.db import models

from accounts.models import User as UserModel
from contentshub.models import Klass, Master


class Question(models.Model):
    """
    Assignee : 상백

    User 모델과 1:N 관계를 가지고, Klass 모델과 1:N 관계를 가지는 Question 모델입니다.
    1명의 유저가 여러 개의 질문을 남길 수 있도록 설정합니다.
    또한, 삭제가 진행되는 경우 is_deleted 필드를 True로 변경합니다.
    """

    user = models.ForeignKey(to=UserModel, verbose_name="수강생", on_delete=models.CASCADE, related_name="user_question")
    klass = models.ForeignKey(to=Klass, verbose_name="강의", on_delete=models.CASCADE, related_name="klass_question")
    contents = models.TextField("내용", max_length=200)
    is_deleted = models.BooleanField("삭제여부", default=False)
    created_at = models.DateTimeField("생성일", auto_now_add=True)
    updated_at = models.DateTimeField("수정일", auto_now=True)


class Answer(models.Model):
    """
    Assignee : 상백

    Question 모델과 1:1 관계를 가지고, Master 모델과 1:N 관계를 가지는 Answer 모델입니다.
    1개의 질문에 1개의 답변이 달리고, 1명의 강사가 여러 개의 질문을 남길 수 있도록 설정합니다.
    """

    question = models.OneToOneField(
        to="Question", verbose_name="질문", on_delete=models.CASCADE, related_name="question_answer"
    )
    master = models.ForeignKey(to=Master, verbose_name="강사", on_delete=models.CASCADE, related_name="master_answer")
    contents = models.TextField("내용", max_length=500)
    created_at = models.DateTimeField("생성일", auto_now_add=True)
    updated_at = models.DateTimeField("수정일", auto_now=True)
