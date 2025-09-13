from .models import Product

class ProductService:
    """ Класс реализующий интерфейс сервисных функций """

    @staticmethod
    def list_product_by_category(category):
        """ Функция возвращает список товаров в указанной категории """
        return Product.objects.filter(category=category)
