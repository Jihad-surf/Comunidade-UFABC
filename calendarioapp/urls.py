from django.urls import path
from calendarioapp.views import index

urlpatterns = [ 
    path('',index),
]