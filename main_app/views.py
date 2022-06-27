from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Requirements
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile
from .models import Job, Requirements
from .forms import RequirementsForm
# Create your views here.


# home URL
def home(request):
    return render(request, 'home.html')

# about URL
def about(request):
    return render(request, 'about.html')

# Job URL
def jobs_index(request):
    jobs = Job.objects.filter(user = request.user)
    # Filter will go here
    return render(request, 'jobs/index.html', {'jobs': jobs})

class JobCreate(CreateView):
    model = Job
    fields = ['title', 'company', 'contract_type', 'salary', 'link', 'description', 'contact']

    def form_valid(self, form):
        # form.instance.user = self.request.user
        return super().form_valid(form)
    

class JobUpdate(UpdateView):
    model = Job
    fields = ['title', 'company', 'contract_type', 'salary', 'link', 'description', 'contact']


class JobDelete(DeleteView):
    model = Job
    success_url = '/jobs/'


def jobs_detail(request, job_id):
    job = Job.objects.get(id=job_id)
    requirements_form = RequirementsForm
    requirements_to_get_job = Requirements.objects.filter(user = request.user).exclude(id__in = job.requirements.all().values_list('id'))
    return render(request, 'jobs/details.html', {'job': job, 'title': "Jobs Details Page", 'requirements_form': requirements_form, 'requirements': requirements_to_get_job})


    
# Requirements URLs

def add_requirement(request, job_id):
    form = RequirementsForm(request.POST)

    if form.is_valid():
        new_requirement = form.save(commit=False)
        new_requirement.job_id = job_id
        new_requirement.save()
        return redirect('detail', job_id = job_id)


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

def requirements_index(request):
    requirements_list = Requirements.objects.filter(user = request.user)
    return render(request, 'main_app/requirement_list.html', {'requirements_list': requirements_list})


# User and profile views

def profile(request):
    return render(request, 'accounts/profile.html')
  

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


# class ProfileCreate(CreateView):
#     model = Profile
#     fields = ['phone', 'city', 'zipcode']


# class ProfileUpdate(UpdateView):
#     model = Profile
#     fields = ['phone', 'city', 'zipcode']
#     success_url = '/profile/'


# class UserUpdate(UpdateView):
#     model = User
#     fields = ['first_name', 'last_name', 'email']
#     success_url = '/profile/'