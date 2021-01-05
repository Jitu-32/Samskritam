from django import forms
from django.forms import ModelForm
from .models import *



class CompetitionForm(ModelForm):
    class Meta:
        model = Competition
        fields = ['name','description']







