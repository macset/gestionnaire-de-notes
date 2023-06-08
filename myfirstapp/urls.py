from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('enseignement/', views.enseignement, name='enseignement'),
    path('main/', views.main, name='main'),
]
