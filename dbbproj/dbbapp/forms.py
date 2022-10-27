from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Userdb

class UserForm(forms.ModelForm):
    class Meta:
        model = Userdb
        fields = "__all__"
        