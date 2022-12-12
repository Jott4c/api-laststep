from rest_framework_simplejwt.views import TokenObtainPairView
from django.urls import path
from . import views


urlpatterns = [
    path("users/", views.UserView.as_view()),
    path("users/<int:user_id>/", views.UserDetailView.as_view()),
    path("users/login/", TokenObtainPairView.as_view()),
]
