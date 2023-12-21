from django.urls import path
from .views import *

urlpatterns = [
      
    path("", textclassifier, name="textclassifier"),
     
]