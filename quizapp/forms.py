from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from .models import Profile

class DatePicker(forms.DateInput):
    input_type = 'date'

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')

COLLEGES = (
    ('D.J Sanghvi','D.J Sanghvi'),
    ('IIT Powai','IIT Powai'),
    ('IIIT Delhi','IIIT Delhi'),
    ('VJTI','VJTI'),

)

class ProfileForm(forms.Form):
    course = forms.CharField()
    col_name = forms.ChoiceField(choices=COLLEGES)
    birth_date = forms.DateField(widget=DatePicker)
    # class Meta:
    #     model = Profile
    #     fields = ('course', 'col_name', 'birth_date')




    
    