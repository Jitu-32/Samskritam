from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
# Create your models here.

'''
Foreign Key: Many to One
One to Many
'''

class Competition(models.Model):
    name = models.TextField()
    organiser = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    description = models.TextField(default='-')
    start_time = models.DateTimeField(null = True,auto_now = True)
    end_time = models.DateTimeField(null = True,auto_now = True)

    def __str__(self):
        return self.name

class Student_data(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    education_level = models.IntegerField(choices=[(1,"Class 1"),(2,"Class 2"),(3,"Class 3"),(4,"Class 4"),(5,"Class 5"),(6,"Class 6"),(7,"Class 7"),(8,"Class 8"),(9,"Class 9"),(10,"Class 10"),(11,"Class 11"),(12,"Class 12"),(13,"Undergrad"),(14,"Graduate")])        

class Expert_data(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=200)
    age = models.IntegerField()

class Pdf_question(models.Model):
    contest = models.ForeignKey(Competition,on_delete=models.SET_NULL,null=True,related_name='pdf_question')
    question = models.TextField(null = True,blank = True)

class Pdf_student_response(models.Model):
    contest = models.ManyToManyField(Competition)
    student = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    fileurl = models.TextField(null = True, blank = True,default='-')
    filename = models.TextField(null = True, blank =True,default='-')    

class MCQ_question(models.Model):
    contest = models.ForeignKey(Competition,on_delete=models.SET_NULL,null=True,related_name='mcq_question')
    question = models.TextField(null = True,blank = True)

class MCQ_option(models.Model):
    question = models.ForeignKey(MCQ_question,on_delete=models.SET_NULL,null=True,related_name='mcq_option')    
    option = models.TextField(null = True,blank = True)

class MCQ_correct_response(models.Model):
    question =  models.ForeignKey(MCQ_question,on_delete=models.SET_NULL,null=True,related_name='mcq_correct_question')
    answer = models.ForeignKey(MCQ_option,on_delete=models.SET_NULL,null=True,related_name='MCQ_correct_response')

class MCQ_student_response(models.Model):
    question =  models.ForeignKey(MCQ_question,on_delete=models.SET_NULL,null=True,related_name='mcq_student_question')
    student = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='mcq_student')
    response = models.ForeignKey(MCQ_option,on_delete=models.SET_NULL,null=True,related_name='MCQ_student_response') 

class FIB_question(models.Model):
    contest = models.ForeignKey(Competition,on_delete=models.SET_NULL,null=True)
    question = models.TextField(null = True,blank = True)


class FIB_student_response(models.Model):
    question =  models.ForeignKey(FIB_question,on_delete=models.SET_NULL,null=True)
    student = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    response = models.TextField(null = True,blank = True)

