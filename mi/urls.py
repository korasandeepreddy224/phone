from django.urls import path
from mi.views import *

urlpatterns = [
    path('phone/',phone,name='phone'),
    
]