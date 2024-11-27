from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def phone(request):
    return HttpResponse('<h1>iphone is the best camera and gameing phone</h1>')
