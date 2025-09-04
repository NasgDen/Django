from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import RegistrationView, EditCustomUser
from users.apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    path('registration/', RegistrationView.as_view(), name="registration"),
    path('login/', LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', LogoutView.as_view(next_page='catalog:products'), name="logout"),
    path('edit_user/<int:pk>/', EditCustomUser.as_view(), name='edit_user'),
]
