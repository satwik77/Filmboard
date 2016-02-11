from registration.models import *
from django.contrib.auth.models import User
from django import forms
from django.utils import timezone



ct= (
    ('Alwar','Alwar'),
    ('Bahadurgarh','Bahadurgarh'),
    ('Bangalore','Bangalore'),
    ('Bareilly','Bareilly'),
    ('Bellary','Bellary'),
    ('Berhampur','Berhampur'),
    ('Bahadurgarh','Bahadurgarh'),
    ('Bhilai','Bhilai'),
    ('Bhiwani','Bhiwani'),
    ('Bhopal','Bhopal'),
    ('Bhubaneswar','Bhubaneswar'),
    ('Bikaner','Bikaner'),
    ('Bilaspur','Bilaspur'),
    ('Chandigarh','Chandigarh'),
    ('Chennai','Chennai'),
    ('Chirawa','Chirawa'),
    ('Chitoor','Chitoor'),
    ('Chittorgarh','Chittorgarh'),
    ('Cochin','Cochin'),
    ('Coimbatore','Coimbatore'),
    ('Dehradun','Dehradun'),
    ('Deogarh','Deogarh'),
    ('Dindigul','Dindigul'),
    ('Faridabad','Faridabad'),
    ('Faridkot','Faridkot'),
    ('Gandhinagar','Gandhinagar'),
    ('Ghaziabad','Ghaziabad'),
    ('Goa','Goa'),
    ('Guna','Guna'),
    ('Guntur','Guntur'),
    ('Gurgaon','Gurgaon'),
    ('Gwalior','Gwalior'),
    ('Hamirpur','Hamirpur'),
    ('Hissar','Hissar'),
    ('Hyderabad','Hyderabad'),
    ('Indore','Indore'),
    ('Jaipur','Jaipur'),
    ('Jammu','Jammu'),
    ('Jhajjar','Jhajjar'),
    ('Jhalawar','Jhalawar'),
    ('Jhansi','Jhansi'),
    ('Jhunjhunu','Jhunjhunu'),
    ('Jodhpur','Jodhpur'),
    ('Kannur','Kannur'),
    ('Kanpur','Kanpur'),
    ('Kharagpur','Kharagpur'),
    ('Kolkata','Kolkata'),
    ('Kota','Kota'),
    ('Kurukshetra','Kurukshetra'),
    ('Lakshmangarh','Lakshmangarh'),
    ('Latur','Latur'),
    ('Lucknow','Lucknow'),
    ('Madurai','Madurai'),
    ('Mandi','Mandi'),
    ('Mathura','Mathura'),
    ('Meerut','Meerut'),
    ('Mohali','Mohali'),
    ('Moradabad','Moradabad'),
    ('Mumbai','Mumbai'),
    ('Nagpur','Nagpur'),
    ('Narasaraopet','Narasaraopet'),
    ('Nashik','Nashik'),
    ('Neemrana','Neemrana'),
    ('Nellore','Nellore'),
    ('New Delhi','New Delhi'),
    ('Noida','Noida'),
    ('Panipat','Panipat'),
    ('Patiala','Patiala'),
    ('Patna','Patna'),
    ('Pilani','Pilani'),
    ('Pondicherry','Pondicherry'),
    ('Pune','Pune'),
    ('Rohtak','Rohtak'),
    ('Roorkee','Roorkee'),
    ('Rupnagar','Rupnagar'),
    ('Sadopur','Sadopur'),
    ('Saharanpur','Saharanpur'),
    ('Salem','Salem'),
    ('Sambalpur','Sambalpur'),
    ('Sangur','Sangur'),
    ('Sarang','Sarang'),
    ('Shimla','Shimla'),
    ('Sikar','Sikar'),
    ('Sonepat','Sonepat'),
    ('Srikakulam','Srikakulam'),
    ('Srinagar','Srinagar'),
    ('Surathkal','Surathkal'),
    ('Tiruchengode','Tiruchengode'),
    ('Thiruvananthapuram','Thiruvananthapuram'),
    ('Udaipur','Udaipur'),
    ('Ujjain','Ujjain'),
    ('Vadodara','Vadodara'),
    ('Varanasi','Varanasi'),
    ('Vellore','Vellore'),
    ('Vijayawada','Vijayawada'),
    ('Vilani','Vilani'),
    ('Villupuram','Villupuram'),
    ('Vishakapatnam','Vishakapatnam'),
    ('Vizag','Vizag'),
    ('Warangal','Warangal'),
    ('Other','Other'),
    )












GENDER= (('M', 'Male'),
         ('F', 'Female'),
         )
CATEGORY= (('legal', 'legal'),
         ('Catering', 'Catering'),
         ('Travel', 'Travel'),
         ('Coordinations', 'Coordinations'),
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
        fields = ('name', 'gender','height','weight','phone','location')
        widgets = {
            'gender': forms.Select(choices=GENDER),
            'location': forms.Select(choices=ct),
        }

class AlliedForm(forms.ModelForm):
    phone = forms.RegexField(regex=r'^\d{10}$', error_message = ("Enter a valid 10 digit mobile number!"))
    class Meta:
        model = Allied
        fields = ('name','category', 'location', 'phone')
        widgets = {
            'category': forms.Select(choices=CATEGORY),
            'location': forms.Select(choices=ct),
        }


class ProductionForm(forms.ModelForm):
    phone = forms.RegexField(regex=r'^\d{10}$', error_message = ("Enter a valid 10 digit mobile number!"))
    class Meta:
        model = Production
        fields = ('name','aboutus','location' , 'phone')
        widgets = {
            'location': forms.Select(choices=ct),
        }