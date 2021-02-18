from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('professional-list', views.proList, name='proList'),
    path('user-profile', views.userProfile1, name='userProfile1'),
    path('blog-post', views.blogPost, name='blogPost'),
    path('blog', views.blogPage, name='blogPage'),
    path('gui-kit', views.guiKit, name='guiKit'),
    path('profile-company', views.profileCompanyPage, name='profileCompanyPage'),
    path('profile-company_no-tabs', views.profileCompanyPageNoTabs, name='profileCompanyPageNoTabs'),
    path('network', views.networkPage, name='networkPage'),
    path('network-hotkeys', views.networkHotkeysPage, name='networkHotkeysPage'),
    path('network-followers', views.networkFollowersPage, name='networkFollowersPage'),
    path('network-following', views.networkFollowingPage, name='networkFollowingPage'),
]
