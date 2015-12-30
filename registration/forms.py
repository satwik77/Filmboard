from registration.models import Artist
from django.contrib.auth.models import User
from django import forms

GENDER= (('M', 'Male'),
         ('F', 'Female'),
         )

class UserForm(forms.ModelForm):
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