from django.urls import path
from . import views

urlpatterns = [
    path('', views.ajouter_membre, name='membre'),
    path('liste', views.liste_membre, name='liste_membre'),
    path('modifier/<str:pk>', views.modifier_membre, name='modifier_membre'),
    path('supprimer/<str:pk>', views.supprimer_membre, name='supprimer_membre')
]