from django.shortcuts import render, HttpResponse
from .models import Project

# Create your views here.
def profile(req):
    projects = Project.objects.all()
    return HttpResponse(projects)
