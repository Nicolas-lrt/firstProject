from django.urls import path

from compte import views

urlpatterns = [
    path('inscription', views.inscriptionPage, name='inscription'),
    path('acces', views.accesPage, name='acces'),
    path('logout', views.logoutUser, name='logout'),

]
