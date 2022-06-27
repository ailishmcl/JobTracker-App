# import path
from django.urls import URLPattern, path

# from main_app directory import views
from . import views

urlpatterns = [
    path('', views.home, name='home'),


# requirements urls
    path('requirements/', views.RequirementsList.as_view(), name='requirements_index'),
    path('requirements/<int:pk>/', views.RequirementsDetail.as_view(), name='requirements_details'),
    path('requirements/create', views.RequirementsCreate.as_view(), name='requirements_create'),
    path('requirements/<int:pk>/update/', views.RequirementsUpdate.as_view(), name='requirements_update'),
    path('requirements/<int:pk>/delete/', views.RequirementsDelete.as_view(), name='requirements_delete'),

]