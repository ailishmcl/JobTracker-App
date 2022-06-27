from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Job, Requirements
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView


import os

# Create your views here.

class JobCreate(CreateView):
    model = Job
    fields = ['title', 'company', 'contract_type', 'salary', 'link', 'description', 'contact']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

class JobUpdate(UpdateView):
    model = Job
    fields = ['title', 'company', 'contract_type', 'salary', 'link', 'description', 'contact']


class JobDelete(DeleteView):
    model = Job
    success_url = '/jobs/'


# home URL
def home(request):
    os.getenv('NAME')
    return render(request, 'home.html')