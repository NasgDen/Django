from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView, View

from .forms import ProductForm
from .models import Category, Contact, Product
from .services import ProductService


class ProductCreateView(LoginRequiredMixin, CreateView):
    """ Класс реализующий интерфейс для создания товара """
    model = Product
    form_class = ProductForm
    template_name = "catalog/add_product.html"
    success_url = reverse_lazy("catalog:products")

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class PublishProductView(LoginRequiredMixin, View):
    """ Класс реализующий интерфейс для публикации товара """

    def post(self, request, *args, **kwargs):
        product_id = kwargs["pk"]
        product = get_object_or_404(Product, id=product_id)
        if not request.user.has_perm('catalog.can_unpublish_product'):
            return HttpResponseForbidden("У вас нет прав для публикации товара.")
        if product.is_published:
            product.is_published = False
        else:
            product.is_published = True
        product.save()

        return redirect('catalog:product_detail', pk=product_id)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """ Класс реализующий интерфейс для изменения товара """
    model = Product
    form_class = ProductForm
    template_name = "catalog/add_product.html"
    success_url = reverse_lazy("catalog:products")


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

    def get_queryset(self):
        permission = self.request.user.has_perm('catalog.can_unpublish_product')
        return ProductService.get_product_from_cache(permission)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class ProductDetailView(DetailView):
    """ Класс реализующий интерфейс для отображения детальной информации о товаре """
    model = Product
    template_name = "catalog/product.html"
    context_object_name = "product"


class ProductCategoryView(DetailView):
    model = Category
    template_name = "catalog/product_by_category.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.object.id
        context["products"] = ProductService.list_product_by_category(category)
        return context


class ContactListView(ListView):
    """ Класс реализующий интерфейс для отображения списка контактов """
    model = Contact
    template_name = "catalog/contacts.html"
    context_object_name = "contacts"

    def get_queryset(self):
        return Contact.objects.get()
