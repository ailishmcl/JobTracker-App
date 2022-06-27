from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Requirements
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile
from .models import Job, Requirements
# Create your views here.

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


# home URL
def home(request):
    return render(request, 'home.html')


def profile_create(request):
    return ##Path to profile create page
  
def about(request):
    return render(request, 'about.html')


# Job URL
def jobs_index(request):
    # jobs = Job.objects.filter(user = request.user)
    # Filter will go here
    return render(request, 'jobs/index.html')

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile_create')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html/', context)

class ProfileCreate(CreateView):
    model = Profile
    fields = ['phone', 'city', 'zipcode']

def jobs_detail(request, job_id):
    job = Job.objects.get(id=job_id)
    # requirements_form = 
    # Filter will go here
    return render(request, 'jobs/details.html', {'job': job, 'title': "Jobs Details Page", 
    # 'requirements_form': requirements_form
    })


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    success_url = '/profile/'


class ProfileUpdate(UpdateView):
    model = Profile
    fields = ['phone', 'city', 'zipcode']
    success_url = '/profile/'


class UserUpdate(UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email']
    success_url = '/profile/'

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
