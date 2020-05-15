from django.urls import path

from authentication.views import UserRetrieveUpdateAPIView, RegistrationAPIView, LoginAPIView

app_name = 'authentication'

urlpatterns = [
    path('user/', UserRetrieveUpdateAPIView.as_view(), name='user_details'),
    path('users/', RegistrationAPIView.as_view(), name='sign_up'),
    path('users/login/', LoginAPIView.as_view(), name='login')
]
