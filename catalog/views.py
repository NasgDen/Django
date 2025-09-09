from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import ProductForm, ProductModeratorForm
from .models import Contact, Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    """ Класс реализующий интерфейс для создания товара """
    model = Product
    form_class = ProductForm
    template_name = "catalog/add_product.html"
    success_url = reverse_lazy("catalog:products")


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """ Класс реализующий интерфейс для изменения товара """
    model = Product
    form_class = ProductForm
    template_name = "catalog/add_product.html"
    success_url = reverse_lazy("catalog:products")

    def get_form_class(self):
        user = self.request.user
        if user.has_perm("catalog.can_unpublish_product"):
            return ProductModeratorForm
        else:
            return ProductForm


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """ Класс реализующий интерфейс для удаления товара """
    model = Product
    permission_required = "catalog.delete_product"
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
