from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='login')
def accueilBoutique(request):
    return render(request, 'boutique/accueil.html')


@login_required(login_url='login')
def productDetail(request):
    return render(request, 'boutique/productDetail.html')


