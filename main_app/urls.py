# import path
from django.db import models
from django.urls import URLPattern, path



# from main_app directory import views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('jobs/', views.jobs_index, name='index'),
    path('jobs/<int:job_id>/', views.jobs_detail, name='detail'),
    path('jobs/create/', views.JobCreate.as_view(), name='jobs_create'),
    path('jobs/<int:pk>/update/', views.JobUpdate.as_view(), name='jobs_update'),
    path('jobs/<int:pk>/delete/', views.JobDelete.as_view(), name='jobs_delete'),




# requirements urls
    path('requirements/', views.RequirementsList.as_view(), name='requirements_index'),
    path('requirements/<int:pk>/', views.RequirementsDetail.as_view(), name='requirements_detail'),
    path('requirements/create', views.RequirementsCreate.as_view(), name='requirements_create'),
    path('requirements/<int:pk>/update/', views.RequirementsUpdate.as_view(), name='requirements_update'),
    path('requirements/<int:pk>/delete/', views.RequirementsDelete.as_view(), name='requirements_delete'),
    path('accounts/signup/', views.signup, name='signup'),
]