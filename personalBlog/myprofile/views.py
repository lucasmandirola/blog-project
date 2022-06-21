
from django.shortcuts import render
from .models import Project

# Create your views here.
def profile(req):
    projects = Project.objects.all()
    return render(req, 'profile.html')
