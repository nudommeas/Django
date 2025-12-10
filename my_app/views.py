from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello World")

def about(request):
    return HttpResponse("Hello My Name is Nudom")

def hello(request, first_name):
    return HttpResponse(f"Hello {first_name}")

def number(request, num1,num2):
    return HttpResponse(f" Sum: {num1+num2}")

def add(request, num1, num2, num3):
    return HttpResponse(f" total is: {num1+num2+num3}")