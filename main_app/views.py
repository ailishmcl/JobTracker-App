from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Job, Requirements
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
    return render(request, 'home.html')







class RequirementsList(ListView):
    model = Requirements

class RequirementsDetail(DetailView):
    model = Requirements

class RequirementsCreate(CreateView):
    model = Requirements
    fields = '__all__'

class RequirementsUpdate(UpdateView):
    model = Requirements
    fields = '__all__'

class RequirementsDelete(DeleteView):
    model = Requirements
    success_url = '/requirements/'
