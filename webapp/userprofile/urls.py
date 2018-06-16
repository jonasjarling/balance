from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns =[
    path('', views.userprofile, name='profile'),
    path('statistic', views.statistic, name='statistic'),
    url(r'^api/bodystats/', views.get_bodystats, name='stats'),
]
