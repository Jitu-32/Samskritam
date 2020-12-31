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

    return render(request,'main/competition_questions.html')

def competition_leaderboard(request,pk):

    if request.method == 'POST':
        if 'username' in request.POST.keys():
            # print("Hello WOrld!")
            curr_user = authenticate(username=request.POST['username'], password=request.POST['password'])
            login(request,curr_user)
            return(redirect(home))

    return render(request,'main/competition_leaderboard.html')        




