from django import forms
from django.forms import ModelForm, Select
from .models import Requirements, Job


class RequirementsForm(ModelForm):
    class Meta:
        model = Requirements
        fields = ['type']
        widgets = {
            'type': Select()
        }

class StatusForm(ModelForm):
    
    class Meta:
        model = Job
        fields = ['status', 'title', 'company', 'contract_type', 'salary', 'link', 'description', 'contact']
        

