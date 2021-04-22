from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.


@login_required(login_url='login')
def addProject(request):
    return render(request, 'projets/addProject.html')


def devenirPartenaire(request):
    porteur = 0
    for group in request.user.groups.all():
        if group.name == 'porteur-investisseur':
            porteur = 1
    return render(request, 'projets/devenir-partenaire.html', {'porteur': porteur})


def chartePage(request):
    return render(request, 'projets/charte.html')


def commentInvestir(request):
    return render(request, 'projets/comment-investir.html')

@login_required(login_url='login')
def pq_sabonner(request):
    return render(request, 'projets/pourquoi_s-abonner.html')
