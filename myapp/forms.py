from django import forms
from django.contrib.auth.models import User
from .models import Article
from django.forms import ModelForm

class PostForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title','article','Private']
        label = {'title':'Title','article':'Article'}
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'article': forms.Textarea(attrs={'class':'form-control'}),
            }