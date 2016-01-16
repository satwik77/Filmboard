from registration.models import Artist
from django.contrib.auth.models import User
from django import forms
from django.utils import timezone

GENDER= (('M', 'Male'),
         ('F', 'Female'),
         )


class UserForm(forms.ModelForm):
    # last_login=timezone.now()
    # last_login = forms.DataTimeField(widget=forms.HiddenInput(), initial=timezone.now())    
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        widgets = {
            'password': forms.PasswordInput(), 
        }

class ArtistForm(forms.ModelForm):
    phone = forms.RegexField(regex=r'^\d{10}$', error_message = ("Enter a valid 10 digit mobile number!"))
    class Meta:
        model = Artist
        fields = ('name', 'gender', 'dob','height','weight','phone')
        widgets = {
            'gender': forms.Select(choices=GENDER),
        }