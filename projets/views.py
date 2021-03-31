from django.shortcuts import render

# Create your views here.


def addProject(request):
    return render(request, 'projets/addProject.html')
