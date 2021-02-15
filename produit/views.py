from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from client.models import Client


# Create your views here.
@login_required(login_url='acces')
def home(request):
    clients = Client.objects.all()
    context = {'clients': clients}
    return render(request, 'produit/accueil.html', context)
