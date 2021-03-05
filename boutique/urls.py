from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueilBoutique, name='accueilBoutique'),
    path('detail/<str:pk>', views.productDetail, name='productDetail'),
    path('panier/<str:pk>', views.cartPage, name='cartPage'),
    path('/add-to-cart/<str:pk><str:qty>', views.addToCart, name='addToCart'),

]
