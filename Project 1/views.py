from django.http import HttpResponse
from django.shortcuts import render
def list(request):
    return HttpResponse("Hello, world!")

def home(request):
    return render(request, "home.html")