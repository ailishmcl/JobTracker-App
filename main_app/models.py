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
    
    def get_absolute_url(self):
        return reverse('requirements_detail', kwargs = {'pk' : self.id})


class Job(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    contract_type = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)
    link = models.CharField(max_length=150)
    description = models.TextField(max_length=250)
    contact = models.CharField(max_length=150)
    requirements = models.ManyToManyField(Requirements)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('detail', kwargs = {'job_id': self.id})

    def __str__(self):
        return self.title

        



    
