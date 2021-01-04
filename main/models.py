from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
# Create your models here.

'''
Foreign Key: Many to One
One to Many
'''

class Competition(models.Model):
    name = models.CharField(max_length=200)
    organiser = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    description = models.TextField(default='-')
    start_time = models.DateTimeField(null = True)
    end_time = models.DateTimeField(null = True)
    imageurl = models.TextField(null = True, blank = True,default='-')
    imagename = models.TextField(null = True, blank =True,default='-') 

    def __str__(self):
        return self.name

class Attempted_contests(models.Model):
    contest = models.ForeignKey(Competition,on_delete=models.SET_NULL,null=True)
    student = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    evaluated = models.BooleanField(default=False)
    marks = models.IntegerField(default=0)

    def __str__(self):
        return(self.contest.name + " | " + self.student.first_name)




class Student_data(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    education_level = models.IntegerField(choices=[(1,"Class 1"),(2,"Class 2"),(3,"Class 3"),(4,"Class 4"),(5,"Class 5"),(6,"Class 6"),(7,"Class 7"),(8,"Class 8"),(9,"Class 9"),(10,"Class 10"),(11,"Class 11"),(12,"Class 12"),(13,"Undergrad"),(14,"Graduate")])        

    def __str__(self):
        return self.name

class Expert_data(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=200)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class Pdf_question(models.Model):
    contest = models.ForeignKey(Competition,on_delete=models.SET_NULL,null=True,related_name='pdf_question')
    question = models.TextField(null = True,blank = True)
    marks = models.IntegerField(default=0)

    def __str__(self):
        return(self.contest.name + " | " + self.question)

class Pdf_student_response(models.Model):
    contest = models.ManyToManyField(Competition)
    student = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    fileurl = models.TextField(null = True, blank = True,default='-')
    filename = models.TextField(null = True, blank =True,default='-')    
    marks = models.IntegerField(default=0)

    def __str__(self):
        return(self.contest.name + " | " + self.student)

class MCQ_question(models.Model):
    contest = models.ForeignKey(Competition,on_delete=models.SET_NULL,null=True,related_name='mcq_question')
    question = models.TextField(null = True,blank = True)
    marks = models.IntegerField(default=0)

    def __str__(self):
        return(self.contest.name + " | " + self.question)

class MCQ_option(models.Model):
    contest = models.ForeignKey(Competition,on_delete=models.SET_NULL,null=True)
    question = models.ForeignKey(MCQ_question,on_delete=models.SET_NULL,null=True,related_name='mcq_option')  
    correct = models.BooleanField(default=False)  
    option = models.TextField(null = True,blank = True)
    
    def __str__(self):
        return(self.question.question + " | " + self.option)


class MCQ_student_response(models.Model):
    contest = models.ForeignKey(Competition,on_delete=models.SET_NULL,null=True)
    question =  models.ForeignKey(MCQ_question,on_delete=models.SET_NULL,null=True,related_name='mcq_student_question')
    student = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='mcq_student')
    response = models.ForeignKey(MCQ_option,on_delete=models.SET_NULL,null=True,related_name='MCQ_student_response') 
    marks = models.IntegerField(default=0)
    
    def __str__(self):
        return(self.question.question + " | " + self.student.first_name)

class FIB_question(models.Model):
    contest = models.ForeignKey(Competition,on_delete=models.SET_NULL,null=True)
    question = models.TextField(null = True,blank = True)
    marks = models.IntegerField(default=0)

    def __str__(self):
        return(self.contest.name + " | " + self.question)

class FIB_student_response(models.Model):
    contest = models.ForeignKey(Competition,on_delete=models.SET_NULL,null=True)
    question =  models.ForeignKey(FIB_question,on_delete=models.SET_NULL,null=True)
    student = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    response = models.TextField(null = True,blank = True)
    marks = models.IntegerField(default=0)

    def __str__(self):
        return(self.question.question + " | " + self.response)


class Game(models.Model):
    name = models.CharField(max_length=200)
    game_type = models.CharField(max_length=200) 
    description = models.TextField(default='-')
    imageurl = models.TextField(null = True, blank = True,default='-')
    imagename = models.TextField(null = True, blank =True,default='-') 

    def __str__(self):
        return self.name



