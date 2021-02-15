from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from membre.forms import ajout_form
from membre.models import Membre


# Create your views here.
@login_required(login_url='acces')
def ajouter_membre(request):
    form = ajout_form()
    if request.method == 'POST':
        form = ajout_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/membre/liste')

    context = {"form": form}

    return render(request, 'membre/inscription.html', context)


@login_required(login_url='acces')
def liste_membre(request):
    membres = Membre.objects.all()
    context = {'membres': membres}

    return render(request, 'membre/liste_membre.html', context)


@login_required(login_url='acces')
def modifier_membre(request, pk):
    membre = Membre.objects.get(id=pk)
    form = ajout_form(instance=membre)

    if request.method == 'POST':
        form = ajout_form(request.POST, instance=membre)
        if form.is_valid():
            form.save()
            return redirect('/membre/liste')

    context = {"form": form}

    return render(request, 'membre/inscription.html', context)


@login_required(login_url='acces')
def supprimer_membre(request, pk):
    membre = Membre.objects.get(id=pk)
    if request.method == 'POST':
        membre.delete()
        return redirect('/membre/liste')

    context = {'item': membre}
    return render(request, 'membre/supprimer_membre.html', context)
