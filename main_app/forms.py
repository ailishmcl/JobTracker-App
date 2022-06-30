from django import forms
from django.forms import ModelForm, Select
from django import forms
from .models import Requirements, Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Requirements, Job


class RequirementsForm(ModelForm):
    class Meta:
        model = Requirements
        fields = ['type']
        widgets = {
            'type': Select()
        }

class UserRegisterForm(UserCreationForm):
    # email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name','last_name', 'username', 'email', 'password1', 'password2']
        # fields = '__all__'

class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'username']

class ProfileUpdateForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['cv', 'coverletter', 'other', 'image']

class StatusForm(ModelForm):
    
    class Meta:
        model = Job
        fields = ['status', 'feedback']
        

