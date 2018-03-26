from django.conf.urls import url 
from django.contrib import admin 
from blog import views

app_name = 'blog'
urlpattens = [
 path('', views.index, name='index'),
]
 ]