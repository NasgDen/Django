from django import forms
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm, UserCreationForm

from catalog.forms import StyleFormMixin

from .models import CustomUser


class CustomUserCreationForm(StyleFormMixin, UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'password1', 'password2')

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number and not phone_number.isdigit():
            raise forms.ValidationError('Телефонный номер должен состоять только из цифр')
        return phone_number


class CustomProfileForm(StyleFormMixin, UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'first_name', 'last_name', 'phone_number']


class UserPasswordChangeForm(StyleFormMixin, PasswordChangeForm):
    class Meta:
        model = CustomUser
