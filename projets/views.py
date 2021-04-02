from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.


@login_required(login_url='login')
def addProject(request):
    return render(request, 'projets/addProject.html')


def devenirPartenaire(request):
    return render(request, 'projets/devenir-partenaire.html')


def chartePage(request):
    return render(request, 'projets/charte.html')


def commentInvestir(request):
    return render(request, 'projets/comment-investir.html')