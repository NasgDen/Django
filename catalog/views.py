from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


def home(request):
    """ Контроллер для отображения страницы home.html """
    products = Product.objects.order_by('-id')[:5]
    for product in products:
        print(product.name)
    return render(request, "home.html")


def contacts(request):
    """ Контроллер для отображения страницы contacts.html и обработки POST запроса """
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        phone = request.POST.get('phone')
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    return render(request, "contacts.html")
