from rest_framework.serializers import ModelSerializer

from .models import Question


class QuestionModelSerializer(ModelSerializer):
    """
    Assignee : 상백

    create 메소드를 통해 로그인된 유저 및 강의와 1:N 관계에 있는 Question 모델 객체를 생성합니다.
    """

    def create(self, validated_data):
        user = self.context["user"]
        klass = self.context["klass"]
        question = Question(user=user, klass=klass, **validated_data)
        question.save()
        return question

    class Meta:
        model = Question
        fields = ("user", "klass", "contents", "created_at", "updated_at")
        read_only_fields = ["user", "klass", "is_deleted", "created_at"]
