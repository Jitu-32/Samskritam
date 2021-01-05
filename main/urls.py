from django.urls import path
from . import views
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

urlpatterns = [
	path('',views.home,name="home"),
	path('know_more/',views.history,name="history"),
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
	path('new_competition/',views.new_competition,name="new_competition"),
	path('my_competition_student_response/<int:pk>/<int:student_id>/',views.my_competition_student_response,name="my_competition_student_response"),
	path('new_mcq_question/<int:pk>/',views.new_mcq_question,name="new_mcq_question"),
	path('new_mcq_option/<int:pk>/',views.new_mcq_option,name="new_mcq_option"),
	path('new_competition/',views.new_competition,name="new_competition"),
	path('edit_competition/<int:pk>/',views.edit_competition,name="edit_competition"),
	path('new_fib_question/<int:pk>/',views.new_fib_question,name="new_fib_question"),

	path('play/',views.play,name="play"),
	path('play/<str:gamename>/',views.game,name="game"),
	path('play/memorygame_desc',views.memorygame_desc,name="memorygame_desc") ,
	path('play/memorygame',views.memorygame,name="memorygame") ,
	path('play/scramble_desc',views.scramble_desc,name="scramble_desc") ,
	path('play/scramble',views.scramble,name="scramble") ,
	path('test/',views.test,name="test"),



	path('learn/',views.learn,name="learn"),
	path('learn/lesson1',views.lesson1,name='lesson1'),
	path('learn/lesson2',views.lesson2,name='lesson2'),
	path('learn/lesson3',views.lesson3,name='lesson3'),
	path('learn/lesson4',views.lesson4,name='lesson4'),
	path('learn/lesson5',views.lesson5,name='lesson5'),
	path('learn/lesson6',views.lesson6,name='lesson6'),

	path('classes/',views.join_class,name='class'),
	path('video_call/',views.video_call,name='video_call'),


]
