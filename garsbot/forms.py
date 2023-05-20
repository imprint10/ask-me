# forms.py
from django import forms

class AskGarsbotForm(forms.Form):
    question = forms.CharField(widget=forms.Textarea, max_length=500)