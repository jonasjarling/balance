from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from . import views

urlpatterns = (
    path('login/', views.login, name='login'),
    path('news/', views.news, name='news'),
    url(r'^$', views.index, name='index'),
)