from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def phone(request):
    return HttpResponse('<h1>nokia is a best key phone</h1>')