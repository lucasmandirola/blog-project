from django.shortcuts import render, HttpResponse

def index(req):
    return HttpResponse('<h1>Pagina de inicio</h1>')
