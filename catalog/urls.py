from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, product, add_product, success_view

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name="home"),
    path('contacts/', contacts, name="contacts"),
    path('product/<int:id>', product, name="product"),
    path('add_product/', add_product, name="add_product"),
    path('success/', success_view, name="success"),
]
