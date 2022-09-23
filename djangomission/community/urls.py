from django.urls import path

from .views import AnswerCreateAPIView, QuestionCreateAPIView, QuestionDeleteAPIView

app_name = "community"

urlpatterns = [
    path("api/v1/klasses/<klass_id>", QuestionCreateAPIView.as_view()),
    path("api/v1/questions/<question_id>", QuestionDeleteAPIView.as_view()),
    path("api/v1/questions/<question_id>/answer", AnswerCreateAPIView.as_view()),
]
