from django.contrib import admin
from django.urls import path,include
from librarymanagement import views

urlpatterns = [

    path('',views.index,name='library'),
    path('about',views.about,name='about'),
    path('home',views.home,name='home'),
    path('login',views.user_login,name='login'),
    path('register',views.register,name='register'),
    path('logout',views.user_logout,name='logout'),
   
]