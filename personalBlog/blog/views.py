
from django.shortcuts import render
from .models import Post

# Create your views here.
def posts(req):
    blogs = Post.objects.all()
    return render(req, 'blogs.html')

def post(req, id):
    blog = Post.objects.get(id = id)
    content = f'{blog.title} - {blog.desc}'
    return render(req, 'blog.html')
