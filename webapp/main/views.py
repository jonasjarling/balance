from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
#from .forms import UserForm
from django.views.generic import View

# Create your views here.
def index(request):


    context = {
        'test': '123'
    }
    return render(request, 'main/index.html', context)


def login(request):


    context = {

    }
    return render(request,'main/login.html', context)




def news(request):
    context = {
        'test': '123'
    }
    return render(request, 'main/news.html', context)



def profile(request):
    context = {
        'test': '123'
    }
    return render(request, 'main/profile.html', context)