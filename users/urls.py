from django.urls import path

from catalog.views import (ContactListView, ProductCreateView, ProductDeleteView, ProductDetailView, ProductListView,
                           ProductUpdateView)
from users.apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name="products"),

]
