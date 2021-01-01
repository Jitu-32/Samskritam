from django.urls import path
from . import views
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

urlpatterns = [

	path('',views.home,name="home"),
	path('compete/',views.compete,name="compete"),
	path('logout/',views.logout_view,name="logout_view"),
	path('signup/',views.signup_view,name="signup_view"),
	path('competition_description/<int:pk>/',views.competition_description,name="competition_description"),
	path('competition_questions/<int:pk>/',views.competition_questions,name="competition_questions"),
	path('competition_leaderboard/<int:pk>/',views.competition_leaderboard,name="competition_leaderboard"),
	path('play/',views.play,name="play"),
	path('play/<str:gamename>/',views.game,name="game"),
	path('play/memorygame',views.memorygame,name="memorygame") ,
	
]




    