from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView

from .forms import ProductForm
from .models import Contact, Product


class ProductListView(ListView):
    model = Product
    template_name = "catalog/home.html"
    context_object_name = "products"



# def home(request):
#     """ Контроллер для отображения страницы home.html """
#     products = Product.objects.all().order_by('-id')
#     paginator = Paginator(products, 5)
#     page_number = request.GET.get('page')
#     page_object = paginator.get_page(page_number)
#     # for product in products:
#     #     print(product.name)
#     return render(request, "home.html", {"page_object": page_object})


# def contacts(request):
#     """ Контроллер для отображения страницы contacts.html и обработки POST запроса """
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         message = request.POST.get('message')
#         phone = request.POST.get('phone')
#         return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
#     contacts = Contact.objects.get()
#     return render(request, "contacts.html", {'contacts': contacts})
#
#
# def product(request, pk):
#     """ Контроллер для отображения страницы с подробным описанием товара """
#     product = Product.objects.get(id=pk)
#     return render(request, 'product.html', {'product': product})
#
#
# def add_product(request):
#     """ Контроллер для добавления товаров в базу данных """
#     if request.method == 'POST':
#         form = ProductForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return render(request, 'success.html')
#     else:
#         form = ProductForm()
#     return render(request, 'add_product.html', {'form': form})
#
#
# def success_view(request):
#     return render(request, 'success.html')
