from django.urls import path
from . import views 
urlpatterns = [
    path('', views.home, name='home'),

    path('about/', views.about, name='about'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('api/', views.api_test), 
]

path('api/', views.project_api),
