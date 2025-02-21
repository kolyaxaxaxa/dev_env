from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {
        'title': 'Главная',
        'content': 'Главная страница магазина',
        'prods': {'sku': 1001, 'name': 'Мясорубка Tefal TF 4501', 'price': 4990},
        'list': [True, 125, 'Товар'],
        'bool': False
    }
    return render(request, 'main/index.html', context=context)


def about(request):
    return HttpResponse('О нас')
