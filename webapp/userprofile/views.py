from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse

from .models import Profile, Weight

@login_required
def userprofile(request):
    context = Profile.objects.get(user=request.user).as_dict()
    print(context)
    return render(request, 'userprofile/profile.html', {"context":context})

@login_required
def statistic(request):
    data = Weight.objects.filter(user=request.user)
    context = {}
    for obj in data:
        context[obj] = obj.as_dict()
    return render(request, 'userprofile/statistic.html', {"context": context})
