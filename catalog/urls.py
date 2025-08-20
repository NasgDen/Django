from django.urls import include, path

from catalog.apps import CatalogConfig
# from catalog.views import add_product, contacts, product, success_view, ProductListView
from catalog.views import ProductListView, ProductDetailView, ContactView, ProductCreateView

app_name = CatalogConfig.name

urlpatterns = [
    # path('', home, name="home"),
    path('', ProductListView.as_view(), name="products"),
    path('product/<int:pk>', ProductDetailView.as_view(), name="product_detail"),
    path('contacts/', ContactView.as_view(), name="contacts"),
    path('add_product/', ProductCreateView.as_view(), name="add_product"),

#     path('contacts/', contacts, name="contacts"),
#     path('product/<int:pk>', product, name="product"),
#     path('add_product/', add_product, name="add_product"),
#     path('success/', success_view, name="success"),
]
