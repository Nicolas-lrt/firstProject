from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueilBoutique, name='accueilBoutique'),
    path('detail/<str:pk>', views.productDetail, name='productDetail'),
    path('panier', views.cartPage, name='cartPage'),
    path('recap', views.cartRecap, name='cartRecap'),
    path('add-to-cart/<str:pk><str:qty>', views.addToCart, name='addToCart'),
    path('remove-from-cart/<str:pk>', views.removeFromCart, name='removeFromCart'),
    path('clear-cart/', views.clearCart, name='clearCart'),
    path('clear-cartLine/<str:pk>', views.clearCartLine, name='clearCartLine'),
    path('config/', views.stripe_config),
    path('create-checkout-session/', views.create_checkout_session),
    path('success/', views.SuccessView.as_view()),
    path('cancelled/', views.CancelledView.as_view()),
    path('webhook/', views.stripe_webhook),
    path('create-order/', views.createOrder, name='createOrder'),
    path('orders/', views.orderPage, name='orders'),
    path('order-detail/<str:pk>/', views.orderDetails, name='orderDetail'),

]
