from django.urls import path

from .views import RegistrationView
from users.apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    path('registration/', RegistrationView.as_view(), name="registration"),
]
