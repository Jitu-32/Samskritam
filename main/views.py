from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage
from datetime import *

def home(request):

    login_error = None

    if request.method == 'POST':
        if 'username' in request.POST.keys():
            # print("Hello WOrld!")
            curr_user = authenticate(username=request.POST['username'], password=request.POST['password'])
            try:
                login(request,curr_user)
            except:
                login_error = "The username and password combination is incorrect please check again!"
                return render(request,'main/home.html',{"login_error":login_error})    

            return(redirect(home))

    expert = None

    if request.user.is_authenticated:
        if Expert_data.objects.filter(user = request.user):
            expert = request.user



    return render(request,'main/home.html',{"expert":expert})




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
            try:
                login(request,curr_user)
            except:
                login_error = "The username and password combination is incorrect please check again!"
                return render(request,'main/home.html',{"login_error":login_error})    

            return(redirect(home))

    expert = None

    if request.user.is_authenticated:
        if Expert_data.objects.filter(user = request.user):
            expert = request.user        

    now = datetime.now()
    # print(now)
    live_competitions = Competition.objects.filter(end_time__gte=now)
    past_competitions = Competition.objects.filter(end_time__lt=now)
    # all_competitions = Competition.objects.all()        

    return render(request,'main/compete.html',{"expert":expert,"live_competitions":live_competitions,"past_competitions":past_competitions})  


def my_competitions(request):

    expert = None

    if request.user.is_authenticated:
        if Expert_data.objects.filter(user = request.user):
            expert = request.user

    if not expert:
        return(redirect(home))

    now = datetime.now()

    my_live_competitions = Competition.objects.filter(end_time__gte=now,organiser = expert)
    my_past_competitions = Competition.objects.filter(end_time__lt=now,organiser = expert)

    return render(request,'main/my_competitions.html',{"expert":expert,"live_competitions":my_live_competitions,"past_competitions":my_past_competitions})

def competition_description(request,pk):

    if request.method == 'POST':
        if 'username' in request.POST.keys():
            # print("Hello WOrld!")
            curr_user = authenticate(username=request.POST['username'], password=request.POST['password'])
            try:
                login(request,curr_user)
            except:
                login_error = "The username and password combination is incorrect please check again!"
                return render(request,'main/home.html',{"login_error":login_error})    

            return(redirect(home))

    expert = None

    if request.user.is_authenticated:
        if Expert_data.objects.filter(user = request.user):
            expert = request.user        

    competition = Competition.objects.get(pk=pk)   


    return render(request,'main/competition_description.html',{"expert":expert,"competition":competition})

def my_competition_description(request,pk):

    expert = None

    if request.user.is_authenticated:
        if Expert_data.objects.filter(user = request.user):
            expert = request.user

    if not expert:
        return(redirect(home))

    competition = Competition.objects.get(pk=pk)      

    return render(request,'main/my_competition_description.html',{"expert":expert,"competition":competition})    


def competition_questions(request,pk):
   

    expert = None

    if request.user.is_authenticated:
        if Expert_data.objects.filter(user = request.user):
            expert = request.user            

    competition = Competition.objects.get(pk=pk)

    answered = False
    message = None

    if not request.user.is_authenticated :
        message = "Please login to view the questions"
        return render(request,'main/home.html',{"message":message})



    if Attempted_contests.objects.filter(contest = competition,student = request.user):
        answered = True


    mcq_questions = MCQ_question.objects.filter(contest=competition)
    mcq_options = MCQ_option.objects.filter(contest=competition)  

    fib_questions = FIB_question.objects.filter(contest=competition)

    pdf_questions = Pdf_question.objects.filter(contest=competition)

    fresh = False
    # print(answered)

    if request.method == 'POST':
        # print(request.POST) 
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
        return(redirect(competition_questions,competition.pk))                  

    return render(request,'main/competition_questions.html',{"expert":expert,"answered":answered,"competition":competition,"mcq_options":mcq_options,"mcq_questions":mcq_questions,"fib_questions":fib_questions,"pdf_questions":pdf_questions})


def new_competition(request):
    # need to create a new competition

    expert = None

    if request.user.is_authenticated:
        if Expert_data.objects.filter(user = request.user):
            expert = request.user

    if not expert:
        return(redirect(home))

    
    return render(request,'main/new_competition.html',{"expert":expert})


def new_mcq_question(request,pk):
    # need to create a new opt

    expert = None

    if request.user.is_authenticated:
        if Expert_data.objects.filter(user = request.user):
            expert = request.user

    if not expert:
        return(redirect(home))

    contest = Competition.objects.get(pk=pk)

    new_question = MCQ_question.objects.create(contest=contest,question="")

    # print(new_question)

    
    return(redirect(my_competition_questions,contest.pk))       

def new_mcq_option(request,pk):
    # need to create a new opt

    expert = None

    if request.user.is_authenticated:
        if Expert_data.objects.filter(user = request.user):
            expert = request.user

    if not expert:
        return(redirect(home))

    mcq_question = MCQ_question.objects.get(pk=pk)
    contest = mcq_question.contest

    new_option = MCQ_option.objects.create(contest=mcq_question.contest,question=mcq_question,option="")

    # print(new_question)

    
    return(redirect(my_competition_questions,contest.pk))           



def my_competition_questions(request,pk):

    expert = None

    if request.user.is_authenticated:
        if Expert_data.objects.filter(user = request.user):
            expert = request.user

    if not expert:
        return(redirect(home))

    competition = Competition.objects.get(pk=pk)  

    mcq_questions = MCQ_question.objects.filter(contest=competition)
    mcq_options = MCQ_option.objects.filter(contest=competition)
    # print(mcq_options)

    fib_questions = FIB_question.objects.filter(contest=competition)

    pdf_questions = Pdf_question.objects.filter(contest=competition) 

     
    

    if request.method == 'POST':
        # print(request.POST) 
        for i in request.POST.keys():
            if i[0]=='m':
                # MCQ
                question = MCQ_question.objects.get(pk=int(i[3:]))
                question.question = request.POST[i]
                question.save()
            elif i[0]=='o':
                # print(i)
                option = MCQ_option.objects.get(pk=int(i[3:]))
                option.option = request.POST[i]
                option.save()
            elif i[0]=='c' and i!='csrfmiddlewaretoken':
                # print(i)
                corr_option = MCQ_option.objects.get(pk=int(i[3:]))
                corr_option.correct = True
                corr_option.save()
                

            elif i[0]=='f':
                #FIB
                question = FIB_question.objects.get(pk=int(i[3:]))
                question.question = request.POST[i]
                question.save()
            else:
                #pdf  
                print(i[3:])

        corr_ops = MCQ_option.objects.filter(contest=competition,correct=True)
        for i in corr_ops:
            check_str = "cor"
            check_str += str(i.pk)
            if check_str not in request.POST.keys():
                i.correct = False
                i.save()       

    return render(request,'main/my_competition_questions.html',{"expert":expert,"competition":competition,"mcq_options":mcq_options,"mcq_questions":mcq_questions,"fib_questions":fib_questions,"pdf_questions":pdf_questions})    

def competition_leaderboard(request,pk):

    if request.method == 'POST':
        if 'username' in request.POST.keys():
            # print("Hello WOrld!")
            curr_user = authenticate(username=request.POST['username'], password=request.POST['password'])
            try:
                login(request,curr_user)
            except:
                login_error = "The username and password combination is incorrect please check again!"
                return render(request,'main/home.html',{"login_error":login_error})    

            return(redirect(home))

    expert = None

    if request.user.is_authenticated:
        if Expert_data.objects.filter(user = request.user):
            expert = request.user        

    competition = Competition.objects.get(pk=pk)        

    return render(request,'main/competition_leaderboard.html',{"expert":expert,"competition":competition})        


def my_competition_responses(request,pk):

    expert = None

    if request.user.is_authenticated:
        if Expert_data.objects.filter(user = request.user):
            expert = request.user

    if not expert:
        return(redirect(home))

    competition = Competition.objects.get(pk=pk)    


    attempted_contests = Attempted_contests.objects.filter(contest=competition)  


    return render(request,'main/my_competition_responses.html',{"expert":expert,"competition":competition,"attempted_contests":attempted_contests})


def my_competition_student_response(request,pk,student_id):

    expert = None

    if request.user.is_authenticated:
        if Expert_data.objects.filter(user = request.user):
            expert = request.user

    if not expert:
        return(redirect(home))

    competition = Competition.objects.get(pk=pk)
    student = User.objects.get(pk=student_id)

    # mcq_questions = MCQ_question.objects.filter(contest=competition)
    # mcq_options = MCQ_option.objects.filter(contest=competition)
    # mcq_responses = MCQ_student_response.objects.filter(contest=competition,student = student)
    # print(mcq_options)

    # fib_questions = FIB_question.objects.filter(contest=competition)
    fib_responses = FIB_student_response.objects.filter(contest=competition,student=student)

    pdf_questions = Pdf_question.objects.filter(contest=competition)

    
    return render(request,'main/my_competition_student_response.html',{"expert":expert,"competition":competition,"fib_responses":fib_responses})    


def play(request):

    if request.method == 'POST':
        if 'username' in request.POST.keys():
            # print("Hello WOrld!")
            curr_user = authenticate(username=request.POST['username'], password=request.POST['password'])
            try:
                login(request,curr_user)
            except:
                login_error = "The username and password combination is incorrect please check again!"
                return render(request,'main/home.html',{"login_error":login_error})    

            return(redirect(home))

    now = datetime.now()
    print(now)
    games = Game.objects.all()
    # all_competitions = Competition.objects.all()        

    return render(request,'main/play.html',{"games": games})  
#####

def memorygame_desc(request):

    if request.method == 'POST':
        if 'username' in request.POST.keys():
            # print("Hello WOrld!")
            curr_user = authenticate(username=request.POST['username'], password=request.POST['password'])
            try:
                login(request,curr_user)
            except:
                login_error = "The username and password combination is incorrect please check again!"
                return render(request,'main/home.html',{"login_error":login_error})    

            return(redirect(home))

    return render(request,'main/game/memorygame_description.html')
#####

def game(request,gamename):

    if request.method == 'POST':
        if 'username' in request.POST.keys():
            # print("Hello WOrld!")
            curr_user = authenticate(username=request.POST['username'], password=request.POST['password'])
            try:
                login(request,curr_user)
            except:
                login_error = "The username and password combination is incorrect please check again!"
                return render(request,'main/home.html',{"login_error":login_error})    

            return(redirect(home))

    game = Game.objects.get(name = gamename)   


    return render(request,'main/game.html',{"game":game})    


def memorygame(request):

    if request.method == 'POST':
        if 'username' in request.POST.keys():
            # print("Hello WOrld!")
            curr_user = authenticate(username=request.POST['username'], password=request.POST['password'])
            try:
                login(request,curr_user)
            except:
                login_error = "The username and password combination is incorrect please check again!"
                return render(request,'main/home.html',{"login_error":login_error})    

            return(redirect(home))


    return render(request,'main/game/memorygame.html')




def scramble_desc(request):

    if request.method == 'POST':
        if 'username' in request.POST.keys():
            # print("Hello WOrld!")
            curr_user = authenticate(username=request.POST['username'], password=request.POST['password'])
            try:
                login(request,curr_user)
            except:
                login_error = "The username and password combination is incorrect please check again!"
                return render(request,'main/home.html',{"login_error":login_error})    

            return(redirect(home))


    return render(request,'main/game/scramble_desc.html')    

def scramble(request):

    if request.method == 'POST':
        if 'username' in request.POST.keys():
            # print("Hello WOrld!")
            curr_user = authenticate(username=request.POST['username'], password=request.POST['password'])
            try:
                login(request,curr_user)
            except:
                login_error = "The username and password combination is incorrect please check again!"
                return render(request,'main/home.html',{"login_error":login_error})    

            return(redirect(home))


    return render(request,'main/game/scramble.html')      