from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello World")

def personal(request):
    return HttpResponse("Hello My Name is Nudom")