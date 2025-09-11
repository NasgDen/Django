from django.contrib.auth import login
from django.contrib.auth.views import PasswordChangeView
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.views.generic.edit import CreateView

from config.settings import EMAIL_HOST_USER, EMAIL_USE_SSL, EMAIL_USE_TLS

from .forms import CustomProfileForm, CustomUserCreationForm, UserPasswordChangeForm
from .models import CustomUser


class RegistrationView(CreateView):
    """ Контроллер для регистрации пользователя """
    template_name = 'users/registration.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('catalog:products')

    def form_valid(self, form):
        print(EMAIL_HOST_USER)
        print(EMAIL_USE_TLS)
        print(EMAIL_USE_SSL)
        user = form.save()
        login(self.request, user)
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    def send_welcome_email(self, user_email):
        subject = 'Добро пожаловать в наш интернет магазин'
        message = 'Спасибо, за регистрацию в нашем интернет магазине!'
        from_email = EMAIL_HOST_USER
        recipient_list = [user_email]
        send_mail(subject, message, from_email, recipient_list)


class EditCustomUser(UpdateView):
    """ Контроллер для редактирования профиля пользователя """
    model = CustomUser
    template_name = 'users/edit_user.html'
    form_class = CustomProfileForm
    success_url = reverse_lazy('catalog:products')


class UserPasswordChangeView(PasswordChangeView):
    """ Контроллер для изменения пароля пользователя """
    model = CustomUser
    template_name = 'users/edit_user.html'
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy('catalog:products')
