from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group, User
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from .decorators import unauthenticated_user
from .forms import CreerUtilisateur
from django.contrib import messages
from membre.forms import ajout_form


# Create your views here.

@unauthenticated_user
def inscriptionPage(request):
    form = CreerUtilisateur()
    formMembre = ajout_form()
    if request.method == 'POST':
        form = CreerUtilisateur(request.POST)
        formMembre = ajout_form(request.POST)
        if form.is_valid():
            # formMembre.Meta.fields = [
            #     request.POST.get('username'),
            #     request.POST.get('email'),
            #     request.POST.get('password1'),
            #     request.POST.get('role')
            # ]
            # formMembre.save()

            user = form.save()
            if request.POST.get('role') == 'Entreprise':
                group = Group.objects.get(name='Entreprise')
                group.user_set.add(user)
            elif request.POST.get('role') == 'Investisseur':
                group = Group.objects.get(name='Investisseur')
                group.user_set.add(user)
            elif request.POST.get('role') == 'Posteur de projet':
                group = Group.objects.get(name='Posteur de projet')
                group.user_set.add(user)
            elif request.POST.get('role') == 'Auto-entrepreneur':
                group = Group.objects.get(name='Auto-entrepreneur')
                group.user_set.add(user)

            return redirect('acces')
    context = {'form': form, 'formMembre': formMembre}
    return render(request, 'compte/inscription.html', context)

@unauthenticated_user
def accesPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Utilisateur et/ou Mot de passe incorrect(s)")
    context = {}
    return render(request, 'compte/acces.html', context)


def logoutUser(request):
    logout(request)
    return redirect('acces')
