from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import (ContactListView, ProductCreateView, ProductDeleteView, ProductDetailView, ProductListView,
                           ProductUpdateView, PublishProductView, ProductCategoryView)

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name="products"),
    path('product/<int:pk>', cache_page(60*10)(ProductDetailView.as_view()), name="product_detail"),
    path('contacts/', ContactListView.as_view(), name="contacts"),
    path('add_product/', ProductCreateView.as_view(), name="add_product"),
    path('update_product/<int:pk>/', ProductUpdateView.as_view(), name="update_product"),
    path('delete_product/<int:pk>/', ProductDeleteView.as_view(), name="delete_product"),
    path('product/published/<int:pk>/', PublishProductView.as_view(), name="published_product"),
    path('product/product_by_category/<int:pk>/', ProductCategoryView.as_view(), name="product_by_category"),
]
