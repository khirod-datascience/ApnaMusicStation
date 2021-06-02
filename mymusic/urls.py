from django.contrib import admin
from django.urls import path,include
from mymusic import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="home"),
    path("video", views.video, name="video"),
    path("anu", views.aindex, name="aindex"),
    path('aimage/', views.aimage, name="aimage"),
    path('alogin/', views.aloginPage, name="alogin"),  
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
