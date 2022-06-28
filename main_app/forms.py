from django.forms import ModelForm, Select
from .models import Requirements

class RequirementsForm(ModelForm):
    class Meta:
        model = Requirements
        fields = ['type']
        widgets = {
            'type': Select()
        }

