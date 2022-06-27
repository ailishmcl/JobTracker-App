from django.shortcuts import render

# Create your views here.



# home URL
def home(request):
    return render(request, 'home.html')