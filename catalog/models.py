from django.db import models

from users.models import CustomUser


class Category(models.Model):
    """ Описание полей модель категорий товаров """

    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f"{self.name} - {self.description}"

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    """ Описание полей модель товаров """

    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='images/', verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена')
    is_published = models.BooleanField(default=False, verbose_name="Статус публикации")
    owner = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, related_name='products', verbose_name='Владелец', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_ut = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __str__(self):
        return f"{self.name} - {self.description} - {self.price}"

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        permissions = [('can_unpublish_product', 'can unpublish product')]


class Contact(models.Model):
    """ Описание полей контактных данных """

    country = models.CharField(max_length=150, verbose_name='Страна')
    itn = models.CharField(max_length=150, verbose_name='ИНН')
    address = models.CharField(max_length=150, verbose_name='Адрес')

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
