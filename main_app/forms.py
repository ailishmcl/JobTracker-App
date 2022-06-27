from django.forms import ModelForm
from .models import Requirements

class RequirementsForm(ModelForm):
    class Meta:
        model = Requirements
        fields = ['type']