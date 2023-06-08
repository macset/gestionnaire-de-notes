from django.urls import path
from . import views


urlpatterns = [
  path('login/', views.login_view, name='login'),
  path('', views.main, name='main'),
  path('ajout', views.ajout, name='ajout'),  
  path('traitement', views.traitement , name='traitement'),
  path('all/', views.all, name='all'),
  path('read/<int:id>', views.read, name='read'),
  path('update/<int:id>', views.update, name='update',),
  path('traitementupdate/<int:id>', views.traitementupdate, name='traitementupdate'),
  path('delete/<int:id>', views.delete, name='delete'),
]