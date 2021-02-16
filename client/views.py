from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from client.models import Client

# Create your views here.
from compte.decorators import allowed_users


@login_required(login_url='acces')
@allowed_users(allowed_roles=['Entreprise', 'admin'])
def liste_client(request):
    clients = Client.objects.all()
    context = {'clients': clients}
    return render(request, 'client/liste_client.html', context)
