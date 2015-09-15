from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    content = {'someadjective': "RAD",
               'somename': "Ichi"
               }
    return render(request, 'index.html', content)

def corgi(request):
    return HttpResponse("Corgis R Awesome <a href='./'>Homepage!</a>")

def forum(request):
    return render(request, 'fakeForum.html')