from django.urls import path
from . import views

urlpatterns = [

    path('', views.addProject, name='addProject'),

]