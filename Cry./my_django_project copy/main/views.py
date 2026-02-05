from django.shortcuts import render

# Логика главной страницы
def home(request):
    # Эти данные Django прогонит через цикл {% for %} в home.html
    context = {
        'title': 'Главная',
        'features': [
            'Наследование шаблонов (Base.html)',
            'Работа со статикой (CSS)',
            'Динамические контекстные данные',
            'Django REST Framework API'
        ]
    }
    return render(request, 'main/home.html', context)

# Логика страницы "О нас"
def about(request):
    return render(request, 'main/about.html')

# Логика для страницы товаров (Пункт №1: циклы/условия)
def items_list(request):
    items = [
        {'name': 'Ноутбук', 'price': 50000, 'stock': True},
        {'name': 'Смартфон', 'price': 30000, 'stock': False},
        {'name': 'Наушники', 'price': 5000, 'stock': True},
    ]
    return render(request, 'main/items.html', {'items': items})

from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def api_test(request):
    data = {
        "project": "My Django Project",
        "status": "API is working",
        "tasks_completed": 3
    }
    return Response(data)

from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def project_api(request):
    return Response({
        "status": "success",
        "message": "Django REST API работает корректно!",
        "version": "1.0"
    })