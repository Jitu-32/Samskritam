from django.urls import path
from . import views
from django.shortcuts import render, redirect

urlpatterns = [

	path('',views.home,name="home"),
	path('compete/',views.compete,name="compete"),
	path('logout/',views.logout_view,name="logout_view"),
	path('signup/',views.signup_view,name="signup_view"),
	path('competition_description/<int:pk>/',views.competition_description,name="competition_description"),
	path('competition_questions/<int:pk>/',views.competition_questions,name="competition_questions"),
	path('competition_leaderboard/<int:pk>/',views.competition_leaderboard,name="competition_leaderboard"),
	path('my_competitions/',views.my_competitions,name="my_competitions"),
	path('my_competition_description/<int:pk>/',views.my_competition_description,name="my_competition_description"),
	path('my_competition_questions/<int:pk>/',views.my_competition_questions,name="my_competition_questions"),
	path('my_competition_responses/<int:pk>/',views.my_competition_responses,name="my_competition_responses"),
]