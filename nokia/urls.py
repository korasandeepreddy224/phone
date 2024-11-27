from django.urls import path
from nokia.views import *

urlpatterns = [
    path('phone/',phone,name='phone'),
]