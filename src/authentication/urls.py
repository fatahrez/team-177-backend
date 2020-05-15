from django.urls import path

from src.authentication.views import UserRetrieveUpdateAPIView, RegistrationAPIView, LoginAPIView

app_name = 'authentication'

urlpatterns = [
    path('user/', UserRetrieveUpdateAPIView.as_view()),
    path('users/', RegistrationAPIView.as_view()),
    path('users/login/', LoginAPIView.as_view())
]