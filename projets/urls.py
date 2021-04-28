from django.urls import path
from . import views

urlpatterns = [

    path('add-project/', views.addProject, name='addProject'),
    path('partenaire/', views.devenirPartenaire, name='devenirPartenaire'),
    path('charte/', views.chartePage, name='chartePage'),
    path('comment-investir/', views.commentInvestir, name='commentInvestir'),
    path('devenir-porteur-investisseur', views.pq_sabonner, name='sabonner'),
    path('config/', views.stripe_config),
    path('create-checkout-session/', views.create_checkout_session),
    path('success/', views.SuccessView.as_view()),
    path('cancelled/', views.CancelledView.as_view()),
    path('partner/', views.newPartner),

]