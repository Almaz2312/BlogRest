from django.urls import path

from post.views import PostAPIView

urlpatterns = [
    path("", PostAPIView.as_view()),
]
