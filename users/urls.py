from django.urls import path
from users.views import LoginAPIView


urlpatterns = [
    path('login', LoginAPIView.as_view(), name='login'),
]
