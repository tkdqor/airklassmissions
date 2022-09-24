from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from contentshub.models import Klass

from .models import Answer, Question


class KlassModelSerializer(ModelSerializer):
    """
    Assignee : 상백

    SerializerMethodField를 사용하여 특정 강의에 속하는 질문 객체들을 조회하는 필드를 설정합니다.
    """

    questions = serializers.SerializerMethodField(required=False)

    def get_questions(self, obj):
        questions = obj.klass_question.order_by("-created_at").filter(is_deleted=False)  # noqa
        questions_serializer = QuestionModelSerializer(questions, many=True)
        return questions_serializer.data

    class Meta:
        model = Klass
        fields = ("id", "master", "title", "summary", "questions", "created_at", "updated_at")  # noqa


class QuestionModelSerializer(ModelSerializer):
    """
    Assignee : 상백

    create 메소드를 통해 로그인된 유저 및 강의와 1:N 관계에 있는 Question 모델 객체를 생성합니다.
    SerializerMethodField를 사용하여 특정 질문에 달린 답변 객체를 조회하는 필드를 설정합니다.
    """

    answer = serializers.SerializerMethodField(required=False)

    def get_answer(self, obj):
        if hasattr(obj, "question_answer"):
            answer = obj.question_answer
        else:
            answer = None
        answer_serializer = AnswerModelSerializer(answer)
        return answer_serializer.data

    def create(self, validated_data):
        user = self.context["user"]
        klass = self.context["klass"]
        question = Question(user=user, klass=klass, **validated_data)
        question.save()
        return question

    class Meta:
        model = Question
        fields = ("user", "klass", "contents", "created_at", "updated_at", "answer")  # noqa
        read_only_fields = ["user", "klass", "is_deleted", "created_at", "updated_at", "answer"]  # noqa


class AnswerModelSerializer(ModelSerializer):
    """
    Assignee : 상백

    create 메소드를 통해 로그인된 강사와 1:N 관계 및 질문과 1:1 관계에 있는 Answer 모델 객체를 생성합니다.
    """

    def create(self, validated_data):
        question = self.context["question"]
        master = self.context["master"]
        answer = Answer(question=question, master=master, **validated_data)
        answer.save()
        return answer

    class Meta:
        model = Answer
        fields = ("question", "master", "contents", "created_at", "updated_at")
        read_only_fields = ["question", "master", "created_at", "updated_at"]
