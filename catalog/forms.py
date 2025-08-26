from django import forms
from django.core.exceptions import ValidationError

from .models import Product

FORBIDDEN_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class ProductForm(forms.ModelForm):
    """ Класс реализующий интерфейс формы для продукта """
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'price', ]

    def __init__(self, *args, **kwargs):
        """ Настройка атрибутов виджета """

        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите название товара'
        })

        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите описание товара'
        })

        self.fields['image'].widget.attrs.update({
            'class': 'form-control'
        })

        self.fields['category'].widget.attrs.update({
            'class': 'form-control',
        })

        self.fields['price'].widget.attrs.update({
            'class': 'form-control',
        })


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
        print('ЦЕНА',price)
        if price < 0:
            raise ValidationError('Цена не может быть отрицательным значением')
        return price


    def clean_image(self):
        """ Метод проверяет формат и размер загружаемого изображения """

        allowed_format_image = ['jpg', 'jpeg', 'png']
        image = self.cleaned_data.get('image')
        print(type(image))
        print('Изображение ',image)
        if image:
            image_format = image.name.split('.')[-1]
            print('Формат ',image_format)
            print('Размер ', image.size)
            if image.size > 5242880:
                raise ValidationError(f'Файл изображения превышает размер 5Мб. Размер изображения = {round(image.size / 1048576, 2)} Мб.')
            if image_format not in allowed_format_image:
                raise ValidationError('Неправильный формат изображение. Необходимый формат: jpg, jpeg, png')
        return image

