from django.urls import path

from .views import KlassCreateAPIView

app_name = "contentshub"

urlpatterns = [
    path("api/v1/klasses", KlassCreateAPIView.as_view()),
]
