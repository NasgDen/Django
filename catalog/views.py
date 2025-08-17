from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    """ Контроллер для отображения страницы home.html """
    return render(request, "home.html")


def contacts(request):
    """ Контроллер для отображения страницы contacts.html и обработки POST запроса """
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        phone = request.POST.get('phone')
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    return render(request, "contacts.html")
