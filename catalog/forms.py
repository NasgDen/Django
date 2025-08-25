from django import forms
from django.core.exceptions import ValidationError

from .models import Product

FORBIDDEN_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class ProductForm(forms.ModelForm):
    """ Класс реализующий интерфейс формы для продукта """
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'price', ]

    def clean_name(self):
        """ Метод проверяет валидацию поля name на запрещенные слова """

        name = self.cleaned_data.get('name')
        for forbidden_word in FORBIDDEN_WORDS:
            if forbidden_word in name.lower():
                raise ValidationError('Поле "Имя" не должно содержать запрещенные слова')
        return name

    def clean_description(self):
        """ Метод проверяет валидацию поля description на запрещенные слова """

        description = self.cleaned_data.get('description')
        for forbidden_word in FORBIDDEN_WORDS:
            if forbidden_word in description.lower():
                raise ValidationError('Поле "Описание" не должно содержать запрещенные слова')
        return description



