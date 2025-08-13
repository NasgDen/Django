from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Добавление продуктов в базу данных'

    def handle(self, *args, **kwargs):

        Category.objects.all().delete()
        Product.objects.all().delete()

        call_command('loaddata', 'category_fixture.json')
        self.stdout.write(self.style.SUCCESS('Successfully loaded data from fixture'))
