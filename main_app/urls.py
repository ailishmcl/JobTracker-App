# import path
from django.db import models
from django.urls import URLPattern, path
from django.contrib.auth import views as auth_views



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
    path('jobs/<int:job_id>/add_requirement/', views.add_requirement, name='add_requirement'),


# requirements urls
    path('requirements/', views.RequirementsList.as_view(), name='requirements_index'),
    path('requirements/<int:pk>/', views.RequirementsDetail.as_view(), name='requirements_detail'),
    path('requirements/create', views.RequirementsCreate.as_view(), name='requirements_create'),
    path('requirements/<int:pk>/update/', views.RequirementsUpdate.as_view(), name='requirements_update'),
    path('requirements/<int:pk>/delete/', views.RequirementsDelete.as_view(), name='requirements_delete'),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/profile/', views.profile, name='profile'),
  
# M/M
    path('jobs/<int:job_id>/assoc_requirement/<int:requirement_id>/', views.assoc_requirement, name='assoc_requirement'),
    path('jobs/<int:job_id>/unassoc_requirement/<int:requirement_id>/', views.unassoc_requirement, name='unassoc_requirement'),

 # password change and reset URLs
    path('accounts/password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('accounts/password_change_done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('accounts/password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]