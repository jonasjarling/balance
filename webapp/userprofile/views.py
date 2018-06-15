from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse

from .models import Profile

@login_required
def userprofile(request):
    context = {
        'test': '123'
    }
    context = Profile.objects.get(user=request.user).as_dict()
    print(context)
    return render(request, 'userprofile/profile.html', {"context":context})

@login_required
def statistic(request):
    context = ''
    return render(request, 'userprofile/statistic.html', {"context":context})