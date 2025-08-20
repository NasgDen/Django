from django.urls import include, path

from catalog.apps import CatalogConfig
# from catalog.views import add_product, contacts, product, success_view, ProductListView
from catalog.views import ProductListView

app_name = CatalogConfig.name

urlpatterns = [
    # path('', home, name="home"),
    path('', ProductListView.as_view(), name="product"),
#     path('contacts/', contacts, name="contacts"),
#     path('product/<int:pk>', product, name="product"),
#     path('add_product/', add_product, name="add_product"),
#     path('success/', success_view, name="success"),
]
