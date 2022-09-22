from django.urls import path

from .views import QuestionCreateAPIView

app_name = "community"

urlpatterns = [
    path("api/v1/klasses/<klass_id>", QuestionCreateAPIView.as_view()),
]
