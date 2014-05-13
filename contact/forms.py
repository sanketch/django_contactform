__author__ = 'Sanket'
from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()
    name = forms.CharField(max_length=100)
    cc_myself = forms.BooleanField(required=False)