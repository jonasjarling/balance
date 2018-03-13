from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from . import views

urlpatterns = (
    url('^login/$', views.UserFormView.as_view(), name='login'),
    path('news/', views.news, name='news'),
    url(r'^$', views.index, name='index'),
)