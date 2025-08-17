from django.urls import include, path

from catalog.apps import CatalogConfig
from catalog.views import add_product, contacts, home, product, success_view

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name="home"),
    path('contacts/', contacts, name="contacts"),
    path('product/<int:pk>', product, name="product"),
    path('add_product/', add_product, name="add_product"),
    path('success/', success_view, name="success"),
]
