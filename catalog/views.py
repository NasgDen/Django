from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Contact, Product
from .forms import ProductForm


class ProductCreateView(CreateView):
    """ Класс реализующий интерфейс для создания товара """
    model = Product
    form_class = ProductForm
    template_name = "catalog/add_product.html"
    success_url = reverse_lazy("catalog:products")


class ProductUpdateView(UpdateView):
    """ Класс реализующий интерфейс для изменения товара """
    model = Product
    form_class = ProductForm
    template_name = "catalog/add_product.html"
    success_url = reverse_lazy("catalog:products")


class ProductDeleteView(DeleteView):
    """ Класс реализующий интерфейс для удаления товара """
    model = Product
    template_name = "catalog/product_confirm_delete.html"
    success_url = reverse_lazy("catalog:products")


class ProductListView(ListView):
    """ Класс реализующий интерфейс для отображения списка товаров """
    model = Product
    template_name = "catalog/home.html"
    context_object_name = "products"
    paginate_by = 5


class ProductDetailView(DetailView):
    """ Класс реализующий интерфейс для отображения детальной информации о товаре """
    model = Product
    template_name = "catalog/product.html"
    context_object_name = "product"


class ContactListView(ListView):
    """ Класс реализующий интерфейс для отображения списка контактов """
    model = Contact
    template_name = "catalog/contacts.html"
    context_object_name = "contacts"

    def get_queryset(self):
        return Contact.objects.get()
