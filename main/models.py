from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
# Create your models here.


class Competition(models.Model):
    name = models.TextField()
    organiser = models.ManyToManyField(User)
    description = models.TextField(default='-')
    start_time = models.DateTimeField(null = True,auto_now = True)
    end_time = models.DateTimeField(null = True,auto_now = True)

    def __str__(self):
        return self.name


class Pdf_question(models.Model):
    contest = models.ForeignKey(Competition,on_delete=models.SET_NULL,null=True,related_name='pdf_question')
    question = models.TextField(null = True,blank = True)

class Pdf_student_response(models):
    contest = models.ManyToManyField(Competition)
    student = models.ManyToManyField(User)
    fileurl = models.TextField(null = True, blank = True,default='-')
    filename = models.TextField(null = True, blank = True,default='-')    

class MCQ_question(models.Model):
    contest = models.ForeignKey(Competition,on_delete=models.SET_NULL,null=True,related_name='mcq_question')
    question = models.TextField(null = True,blank = True)

class MCQ_option(models):
    question = models.ForeignKey(MCQ_question,on_delete=models.SET_NULL,null=True,related_name='mcq_option')    
    option = models.TextField(null = True,blank = True)

class MCQ_correct_response(models):
    question =  models.ForeignKey(MCQ_question,on_delete=models.SET_NULL,null=True,related_name='mcq_correct_question')
    answer = models.ForeignKey(MCQ_option,on_delete=models.SET_NULL,null=True,related_name='MCQ_correct_response')

class MCQ_student_response(models):
    question =  models.ForeignKey(MCQ_question,on_delete=models.SET_NULL,null=True,related_name='mcq_student_question')
    student = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='mcq_student')
    response = models.ForeignKey(MCQ_option,on_delete=models.SET_NULL,null=True,related_name='MCQ_student_response') 







