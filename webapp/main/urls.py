
from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = (
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    #url('^login/$', views.UserFormView.as_view(), name='login'),
    path('news/', views.news, name='news'),
    url(r'^$', views.index, name='index'),
)