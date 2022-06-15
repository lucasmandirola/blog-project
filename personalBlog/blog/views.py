from django.shortcuts import render, HttpResponse
from .models import Post

# Create your views here.
def posts(req):
    blogs = Post.objects.all()
    return HttpResponse(blogs)

def post(req, id):
    blog = Post.objects.get(id = id)
    content = f'{blog.title} - {blog.desc}'
    return HttpResponse(content)
