from django.urls import path
from . import views

urlpatterns = [

    path('add-project/', views.addProject, name='addProject'),
    path('devenir-partenaire/', views.devenirPartenaire, name='devenirPartenaire'),
    path('charte/', views.chartePage, name='chartePage'),
    path('comment-investir/', views.commentInvestir, name='commentInvestir'),

]