from django.shortcuts import render
from .models import Profile,Projects,Review

# Create your views here.

def index(request):
    projects = Projects.objects.all()
    return render(request,'index.html',{"projects":projects})
