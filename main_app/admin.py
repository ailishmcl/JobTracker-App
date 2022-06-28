from django.contrib import admin
from .models import Requirements, Job, Profile

# Register your models here.
admin.site.register(Job)
admin.site.register(Requirements)
admin.site.register(Profile)