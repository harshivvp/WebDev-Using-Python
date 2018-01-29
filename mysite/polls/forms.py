from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):

    class Meta: #Info about your class

        password = forms.CharField(widget=forms.PasswordInput)

        model = User
        fields = ['username','email','password']