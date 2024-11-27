from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def phone(request):
    return HttpResponse('<marquee><h1>mi phone like redmi,poco</h1></marquee>')
