from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage
from datetime import *

def home(request):

    if request.method == 'POST':
        if 'username' in request.POST.keys():
            # print("Hello WOrld!")
            curr_user = authenticate(username=request.POST['username'], password=request.POST['password'])
            login(request,curr_user)
            return(redirect(home))


    return render(request,'main/home.html')

def logout_view(request):
    logout(request)

    return(redirect(home))

def signup_view(request):

    message = None

    if request.method =='POST':

        if request.POST['password']==request.POST['confirm_password']:
            try:
                user = User.objects.create(username=request.POST['username'])
                user.set_password(request.POST['password'])
                user.first_name = request.POST['name']
                user.save()
                # print(request.POST['username'])
                # print(request.POST['password'])
                # print(request.POST['name'])
                login(request,user)
                return(redirect(home))
            except:
                message = "This username has already been taken please choose another one."
                return render(request,'main/signup.html',{"message":message})
                    

    # print("SIGNUP")

    return render(request,'main/signup.html',{"message":message}) 

def compete(request):

    if request.method == 'POST':
        if 'username' in request.POST.keys():
            # print("Hello WOrld!")
            curr_user = authenticate(username=request.POST['username'], password=request.POST['password'])
            login(request,curr_user)
            return(redirect(home))

    now = datetime.now()
    print(now)
    live_competitions = Competition.objects.filter(end_time__gte=now)
    past_competitions = Competition.objects.filter(end_time__lt=now)
    # all_competitions = Competition.objects.all()        

    return render(request,'main/compete.html',{"live_competitions":live_competitions,"past_competitions":past_competitions})  


def competition_description(request,pk):

    if request.method == 'POST':
        if 'username' in request.POST.keys():
            # print("Hello WOrld!")
            curr_user = authenticate(username=request.POST['username'], password=request.POST['password'])
            login(request,curr_user)
            return(redirect(home))

    competition = Competition.objects.get(pk=pk)   


    return render(request,'main/competition_description.html',{"competition":competition})

def competition_questions(request,pk):

    if request.method == 'POST':
        if 'username' in request.POST.keys():
            # print("Hello WOrld!")
            curr_user = authenticate(username=request.POST['username'], password=request.POST['password'])
            login(request,curr_user)
            return(redirect(home))        

    competition = Competition.objects.get(pk=pk)

    answered = False

    if Attempted_contests.objects.filter(contest = competition,student = request.user):
        answered = True


    mcq_questions = MCQ_question.objects.filter(contest=competition)
    mcq_options = MCQ_option.objects.filter(contest=competition)  

    fib_questions = FIB_question.objects.filter(contest=competition)

    pdf_questions = Pdf_question.objects.filter(contest=competition)

    fresh = False
    # print(answered)

    if request.method == 'POST':
        print(request.POST) 
        for i in request.POST.keys():
            if request.POST[i]:

                if not fresh:
                    fresh = True
                    Attempted_contests.objects.create(contest = competition,student = request.user)

                if i[0]=='m':
                    # MCQ
                    option = MCQ_option.objects.get(pk=int(i[3:]))
                    response = MCQ_student_response.objects.create(question = option.question, student = request.user, response = option)
                elif i[0]=='f':
                    #FIB
                    question = FIB_question.objects.get(pk=int(i[3:]))
                    response = FIB_student_response.objects.create(question = question, student = request.user, response = request.POST[i])
                else:
                    #pdf  
                    print(i[3:])          

    return render(request,'main/competition_questions.html',{"answered":answered,"competition":competition,"mcq_options":mcq_options,"mcq_questions":mcq_questions,"fib_questions":fib_questions,"pdf_questions":pdf_questions})

def competition_leaderboard(request,pk):

    if request.method == 'POST':
        if 'username' in request.POST.keys():
            # print("Hello WOrld!")
            curr_user = authenticate(username=request.POST['username'], password=request.POST['password'])
            login(request,curr_user)
            return(redirect(home))

    competition = Competition.objects.get(pk=pk)        

    return render(request,'main/competition_leaderboard.html',{"competition":competition})        



def play(request):

    if request.method == 'POST':
        if 'username' in request.POST.keys():
            # print("Hello WOrld!")
            curr_user = authenticate(username=request.POST['username'], password=request.POST['password'])
            login(request,curr_user)
            return(redirect(home))

    now = datetime.now()
    print(now)
    games = Game.objects.all()
    # all_competitions = Competition.objects.all()        

    return render(request,'main/play.html',{"games": games})  


def game(request,gamename):

    if request.method == 'POST':
        if 'username' in request.POST.keys():
            # print("Hello WOrld!")
            curr_user = authenticate(username=request.POST['username'], password=request.POST['password'])
            login(request,curr_user)
            return(redirect(home))

    game = Game.objects.get(name = gamename)   


    return render(request,'main/game.html',{"game":game})


def memorygame(request):

    if request.method == 'POST':
        if 'username' in request.POST.keys():
            # print("Hello WOrld!")
            curr_user = authenticate(username=request.POST['username'], password=request.POST['password'])
            login(request,curr_user)
            return(redirect(home))


    return render(request,'main/game/memorygame.html',{"game":game})