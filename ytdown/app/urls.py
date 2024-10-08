from django.contrib import admin
from django.urls import path
from app.views import *
urlpatterns = [
    path('',view=home,name='home')
   ]