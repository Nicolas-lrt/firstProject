from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.


@login_required(login_url='login')
def addProject(request):
    return render(request, 'projets/addProject.html')


@login_required(login_url='login')
def devenirPartenaire(request):
    return render(request, 'projets/devenir-partenaire.html')


@login_required(login_url='login')
def chartePage(request):
    return render(request, 'projets/charte.html')


@login_required(login_url='login')
def commentInvestir(request):
    return render(request, 'projets/comment-investir.html')