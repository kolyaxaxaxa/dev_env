from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели HOME',
    }
    return render(request, 'main/index.html', context=context)


def about(request):
    context = {
        'title': 'Home - О нас',
        'content': 'Информация о магазине',
        'text_on_page': 'Текст о том какой классный этот интернет магазин.'
    }
    return render(request, 'main/about.html', context=context)
