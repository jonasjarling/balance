from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import datetime

from django.http import HttpResponse, HttpResponseRedirect

from .models import Profile, Weight, BodyStats
from .forms import WeightForm, ProfileForm

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
    if args == "fat":
        for obj in datas:
            data +=str(obj.fat_dict)


    for obj in datas:
        data += str(obj.as_dict())
    print(data)
    return JsonResponse({"data":data})


@login_required
def modify_profile(request):
    #new_val = Weight() #.objects.filter(user=request.user).order_by('-date').first()

    profile = Profile.objects.get(user=request.user)
    new_weight = Weight()
    new_bodystats = BodyStats()


    if request.method == "POST":
        profileform = ProfileForm(request.POST, instance=profile)

        if profileform.is_valid():
            #new_val = form.save(commit=False)
            new_weight.user = request.user
            new_weight.date = datetime.date.today()
            new_weight.weight = profileform.weight
            new_weight.save()

            new_bodystats.user = request.user
            new_bodystats.date = datetime.date.today()
            new_bodystats.bone = profileform.bone
            new_bodystats.muscle = profileform.muscle
            new_bodystats.water = profileform.water
            new_bodystats.fat = profileform.fat
            new_bodystats.bmi = profileform.weight/(profileform.height*profileform.height)
            new_bodystats.save()

            profile = profileform.save(commit=False)
            profile.bmi = profileform.weight/(profileform.height*profileform.height)
            profile.save()
            return redirect('profile')

    else:
        profileform = ProfileForm(instance=profile)
        print(profileform.as_p())
    return render(request, 'userprofile/modifyProfile.html', {"profileform": profileform})