from django.urls import path

from . import views

urlpatterns =[
    path('', views.userprofile, name='profile'),
    path('statistic', views.statistic, name='statistic'),
]