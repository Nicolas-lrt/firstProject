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
def registerPage(request):
    form = CreerUtilisateur()
    if request.method == 'POST':
        form = CreerUtilisateur(request.POST)
        if form.is_valid():
            role = request.POST.get('role')
            user = form.save()
            group = Group.objects.get(name=role)
            group.user_set.add(user)
            # if request.POST.get('role') == 'Entreprise':
            #     group = Group.objects.get(name='Entreprise')
            #     group.user_set.add(user)
            # elif request.POST.get('role') == 'Investisseur':
            #     group = Group.objects.get(name='Investisseur')
            #     group.user_set.add(user)
            # elif request.POST.get('role') == 'Posteur de projet':
            #     group = Group.objects.get(name='Posteur de projet')
            #     group.user_set.add(user)
            # elif request.POST.get('role') == 'Auto-entrepreneur':
            #     group = Group.objects.get(name='Auto-entrepreneur')
            #     group.user_set.add(user)
            # elif request.POST.get('role') == 'Auto-entrepreneur':
            #     group = Group.objects.get(name='Auto-entrepreneur')
            #     group.user_set.add(user)
            # elif request.POST.get('role') == 'Auto-entrepreneur':
            #     group = Group.objects.get(name='Auto-entrepreneur')
            #     group.user_set.add(user)

            return redirect('login')
    context = {'form': form}
    return render(request, 'compte/inscription2.html', context)


@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        # username = User.objects.get(email=email.lower()).username
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Utilisateur et/ou Mot de passe incorrect(s)")

    return render(request, 'compte/login.html')


def logoutUser(request):
    logout(request)
    return redirect('home')
