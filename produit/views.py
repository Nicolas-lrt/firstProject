from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
# @login_required(login_url='acces')
def home(request):
    return render(request, 'index.html')


def proList(request):
    return render(request, 'listing-filter.html')


def userProfile1(request):
    return render(request, 'user-profile(layout-1).html')


def blogPost(request):
    return render(request, 'blog-post.html')


def blogPage(request):
    return render(request, 'blog.html')


def guiKit(request):
    return render(request, 'gui-kit.html')


def profileCompanyPage(request):
    return render(request, 'profile_company.html')


def profileCompanyPageNoTabs(request):
    return render(request, 'profile_company-no-tabs.html')


def networkPage(request):
    return render(request, 'user-dashboard(connections)(hotkeys-disabled).html')


def networkHotkeysPage(request):
    return render(request, 'user-profile(usr-dshbrd2).html')


def networkFollowersPage(request):
    return render(request, 'user-dashboard(followers).html')


def networkFollowingPage(request):
    return render(request, 'user-dashboard(following).html')


def crowfondingPage(request):
    return render(request, 'crowfonding.html')


@login_required(login_url='login')
def jackpotPage(request):
    return render(request, 'my-jackpot.html')


@login_required(login_url='login')
def myProjects(request):
    context = {
        'groups': request.user.groups.all()
    }
    return render(request, 'my-projects.html', context)
