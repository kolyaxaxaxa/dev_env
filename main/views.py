from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {
        'title': 'Главная',
        'content': 'Главная страница магазина'
    }
    return render(request, 'main/index.html', context=context)


def about(request):
    return HttpResponse('О нас')
