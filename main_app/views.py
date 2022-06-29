from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Job, Requirements
from .forms import RequirementsForm, UserUpdateForm, ProfileUpdateForm, UserRegisterForm
from django.contrib import messages 
from django.http import HttpResponse, JsonResponse



from .forms import RequirementsForm, StatusForm
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


class JobCreate(LoginRequiredMixin, CreateView):
    model = Job
    fields = ['title', 'company', 'contract_type', 'salary', 'link', 'description', 'contact']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class JobUpdate(LoginRequiredMixin, UpdateView):
    model = Job
    fields = ['status', 'feedback', 'title', 'company', 'contract_type', 'salary', 'link', 'description', 'contact']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# For the modal button on index
def edit_status_index(request, job_id):
    instance = get_object_or_404(Job, id=job_id)
    s_form = StatusForm(instance=instance) 
    if request.method == 'POST':
        s_form = StatusForm(request.POST, instance=instance)

        if s_form.is_valid():
            s_form.save(commit=True)
            # messages.success(request, f'Updated Successfully')

            return HttpResponse(s_form.as_table())
        else:
            print("Not updated, you can 'see details' and edit there")
    return HttpResponse(s_form.as_table())
    


class JobDelete(LoginRequiredMixin, DeleteView):
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


class RequirementsList(LoginRequiredMixin, ListView):
    model = Requirements

class RequirementsDetail(LoginRequiredMixin, DetailView):
    model = Requirements

class RequirementsCreate(LoginRequiredMixin, CreateView):
    model = Requirements
    fields = ['type', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class RequirementsUpdate(LoginRequiredMixin, UpdateView):
    model = Requirements
    fields = ['type', 'description']

class RequirementsDelete(LoginRequiredMixin, DeleteView):
    model = Requirements
    success_url = '/requirements/'

def requirements_index(request):
    requirements_list = Requirements.objects.filter(user = request.user)
    return render(request, 'main_app/requirement_list.html', {'requirements_list': requirements_list})


@login_required
def assoc_requirement(request, job_id, requirement_id):
    Job.objects.filter(user = request.user)
    Job.objects.get(id=job_id).requirements.add(requirement_id)
    return redirect('detail', job_id = job_id)

@login_required
def unassoc_requirement(request, job_id, requirement_id):
    Job.objects.filter(user = request.user)
    Job.objects.get(id=job_id).requirements.remove(requirement_id)
    return redirect('detail', job_id = job_id)


# User and profile views

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Your account has been created and you have been logged in!')
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserRegisterForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your profile information has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        context = {
            'u_form' : u_form,
            'p_form' : p_form
        }
    return render(request, 'accounts/profile.html', context)



