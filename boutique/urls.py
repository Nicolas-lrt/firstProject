from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueilBoutique, name='accueilBoutique'),
    path('detail/<str:pk>', views.productDetail, name='productDetail'),
    path('panier', views.cartPage, name='cartPage'),
    path('add-to-cart/<str:pk><str:qty>', views.addToCart, name='addToCart'),
    path('remove-from-cart/<str:pk>', views.removeFromCart, name='removeFromCart'),
    path('clear-cart/<str:pk>', views.clearCart, name='clearCart'),
    path('clear-cartLine/<str:pk>', views.clearCartLine, name='clearCartLine'),

]
