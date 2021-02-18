from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from client.models import Client


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
    return render(request, 'user-dashboard(connections)(hotkeys-enabled).html')


def networkFollowersPage(request):
    return render(request, 'user-dashboard(followers).html')


def networkFollowingPage(request):
    return render(request, 'user-dashboard(following).html')

