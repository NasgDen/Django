from django import forms
from django.core.exceptions import ValidationError

from .models import Product

FORBIDDEN_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, field in self.fields.items():
            field.widget.attrs['class'] = "form-control"
            if fild_name == 'name':
                field.widget.attrs['placeholder'] = "Введите название товара"
            elif fild_name == 'description':
                field.widget.attrs['placeholder'] = "Введите описание товара"
            elif fild_name == 'is_published':
                field.widget.attrs['class'] = "form-check-input"


class ProductForm(StyleFormMixin, forms.ModelForm):
    """ Класс реализующий интерфейс формы для продукта """
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'price',]

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

    def clean_price(self):
        """ Метод проверяет валидацию поля price на положительное значение """

        price = self.cleaned_data.get('price')
        if price < 0:
            raise ValidationError('Цена не может быть отрицательным значением')
        return price

    def clean_image(self):
        """ Метод проверяет формат и размер загружаемого изображения """

        allowed_format_image = ['jpg', 'jpeg', 'png']
        image = self.cleaned_data.get('image')
        if image:
            image_format = image.name.split('.')[-1]
            if image.size > 5242880:
                raise ValidationError(f'Превышен размер файла 5Мб. Размер{round(image.size / 1048576, 2)} Мб.')
            if image_format not in allowed_format_image:
                raise ValidationError('Неправильный формат изображение. Необходимый формат: jpg, jpeg, png')
        return image


class ProductModeratorForm(StyleFormMixin, forms.ModelForm):
    """ Класс реализующий интерфейс формы модераторов """
    class Meta:
        model = Product
        fields = ['is_published',]