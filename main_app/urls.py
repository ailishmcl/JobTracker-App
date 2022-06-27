# import path
from django.urls import URLPattern, path

# from main_app directory import views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    





]