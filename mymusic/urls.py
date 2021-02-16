from django.contrib import admin
from django.urls import path,include
from mymusic import views

urlpatterns = [
    path("", views.index, name="home"),
    #path("music", views.music, name="music"),
    
]
