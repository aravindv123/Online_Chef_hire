from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('complete/', views.complete_view, name='CompleteRegistration'),
    path('Chef_login/', views.chef_login, name='Cheflogin'),
    path('Chef_signup/', views.chef_signup, name='chef_signup'),  # Corrected path name
    path('chef_view/', views.chef_view, name='chef_view'),
    path('home1/', views.home1, name='home1'),
    path('userhome/', views.userhome, name='userhome'),
    path('userlogin/', views.userlogin, name='userlogin'),
]
