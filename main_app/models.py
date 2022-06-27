from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User 

# Create your models here.




class Requirements(models.Model):
    type = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.type
    
