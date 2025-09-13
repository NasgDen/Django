from django.core.cache import cache

from config.settings import CACHE_ENABLE
from .models import Product

class ProductService:
    """ Класс реализующий интерфейс сервисных функций """

    @staticmethod
    def list_product_by_category(category):
        """ Функция возвращает список товаров в указанной категории """
        return Product.objects.filter(category=category)

    @staticmethod
    def get_product_from_cache(permission):
        """ Функция получает данные по товарам из кеша, если кеш пуст, то из базы данных"""
        if not CACHE_ENABLE:
            if permission:
                return Product.objects.all()
            else:
                return Product.objects.filter(is_published=True)

        key_all = "product_list_all"
        key_is_published = "product_list_is_published"

        if  permission:
            products = cache.get(key_all)
            if products is not None:
                return products
            else:
                products = Product.objects.all()
                cache.set('key_all', products, 60 * 15)
                return products
        else:
            products = cache.get(key_is_published)
            print("Продукты - ", products)
            if products is not None:
                return products
            else:
                products = Product.objects.filter(is_published=True)
                cache.set('key_is_published', products, 60 * 15)
                return products


