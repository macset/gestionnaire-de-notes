from django.urls import path
from . import views


urlpatterns = [
  path('ajout', views.ajout, name='ajout'),  
  path('traitement', views.traitement , name='traitement'),
  path('all/', views.all, name='all'),
  path('read/<int:id>', views.read, name='read'),
  path('update/<int:id>', views.update, name='update',),
  path('traitementupdate/<int:id>', views.traitementudpate, name='traitementupdate'),
  path('delete/<int:id>', views.delete, name='delete'),
  #path('', views.all, name='all')
]