from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .models import Contact, Product


class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'description', 'image', 'category', 'price', ]
    template_name = "catalog/add_product.html"
    success_url = reverse_lazy("catalog:products")


class ProductListView(ListView):
    model = Product
    template_name = "catalog/home.html"
    context_object_name = "products"
    paginate_by = 5


class ProductDetailView(DetailView):
    model = Product
    template_name = "catalog/product.html"
    context_object_name = "product"


class ContactListView(ListView):
    model = Contact
    template_name = "catalog/contacts.html"
    context_object_name = "contacts"

    def get_queryset(self):
        return Contact.objects.get()

