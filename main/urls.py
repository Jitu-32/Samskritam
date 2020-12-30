from django.urls import path
from . import views
from django.shortcuts import render, redirect

urlpatterns = [

	path('',views.home,name="home"),
	path('compete/',views.compete,name="compete"),
	path('logout/',views.logout_view,name="logout_view"),
	path('signup/',views.signup_view,name="signup_view"),
]