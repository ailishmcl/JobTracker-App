from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
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

def about(request):
    return render(request, 'about.html')


# Job URL
def jobs_index(request):
    # jobs = Job.objects.filter(user = request.user)
    # Filter will go here
    return render(request, 'jobs/index.html')


def jobs_detail(request, job_id):
    job = Job.objects.get(id=job_id)
    # Filter will go here
    return render(request, 'jobs/details.html', {'job': job, 'title': "Jobs Details Page", 'requirements_form': requirements_form})




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
