from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from client.models import Client
from commande.models import Commande


# Create your views here.

@login_required(login_url='acces')
def liste_commande(request):
    commandes = Commande.objects.all()
    clients = Client.objects.all()
    context = {'commandes': commandes, 'clients': clients}

    return render(request, 'commande/liste_commande.html', context)
