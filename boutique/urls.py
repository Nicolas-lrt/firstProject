from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueilBoutique, name='accueilBoutique'),
    path('detail', views.productDetail, name='productDetail'),

]