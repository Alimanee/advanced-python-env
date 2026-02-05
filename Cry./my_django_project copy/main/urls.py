from django.urls import path
from . import views  # Точка означает "из этой же папки"

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('api/', views.api_test), # Добавь вот это
]

# Добавь это в список urlpatterns
path('api/', views.project_api),