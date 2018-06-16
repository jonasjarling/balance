from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from django.http import HttpResponse

from .models import Profile, Weight, BodyStats

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


def get_bodystats(request, *args, **kwargs):
    datas = BodyStats.objects.filter(user=request.user)
    data = ""
    for obj in datas:
        data += str(obj.as_dict())
    print(data)
    return JsonResponse({"data":data})
