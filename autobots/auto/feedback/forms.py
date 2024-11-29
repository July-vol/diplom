from django.forms import ModelForm
from django import forms
from .models import FeedBack, FeedBacks


class FeedBackForm(forms.ModelForm):
    class Meta:
        model = FeedBack
        fields = ['name', 'email', 'phone', 'message']


class FeedBacksForm(forms.ModelForm):
    class Meta:
        model = FeedBacks
        fields = ['title', 'memo', 'photo', 'important']
