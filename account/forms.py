from django import forms
from django.contrib.auth.forms import UserCreationForm
from account.models import *
from django.contrib.auth.models import User



class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContacUs
        fields = ("contact_number", "comment",)


