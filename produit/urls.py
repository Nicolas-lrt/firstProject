from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('professional-list', views.proList, name='proList'),
    path('user-pro-profile', views.userProfile1, name='userProfile1'),
    path('blog-post', views.blogPost, name='blogPost'),
    path('blog', views.blogPage, name='blogPage'),
    path('gui-kit', views.guiKit, name='guiKit'),
    path('profile-company', views.profileCompanyPage, name='profileCompanyPage'),
    path('profile-company_no-tabs', views.profileCompanyPageNoTabs, name='profileCompanyPageNoTabs'),
    path('projet-dashboard', views.networkPage, name='networkPage'),
    path('user-profile', views.networkHotkeysPage, name='networkHotkeysPage'),
    path('user-followers', views.networkFollowersPage, name='networkFollowersPage'),
    path('user-following', views.networkFollowingPage, name='networkFollowingPage'),
    path('my-projects', views.myProjects, name='myProjects'),
    path('my-jackpot', views.jackpotPage, name='myJackpot'),
    path('crowfonding', views.crowfondingPage, name='crowfondingPage'),
]
