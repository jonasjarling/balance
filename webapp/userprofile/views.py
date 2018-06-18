from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import JsonResponse
import datetime

from django.http import HttpResponse, HttpResponseRedirect

from .models import Profile, Weight, BodyStats
from .forms import WeightForm, ProfileForm, WaageForms

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

@staff_member_required
def admin_update_profile(request):
    profile = Profile.objects.get(user=request)
    if request.method == "POST":
        forms ={}
    else:
        forms = WaageForms()
    return render(request, 'userprofile/adminpush.html', {"forms": forms})

def get_balance_values(request, *args, **kwargs):
    if args == "user":
        profile = Profile.objects.get(user=args)


@login_required
def modify_profile(request):
    #new_val = Weight() #.objects.filter(user=request.user).order_by('-date').first()

    profile = Profile.objects.get(user=request.user)
    new_weight = Weight()
    new_bodystats = BodyStats()


    if request.method == "POST":
        profileform = ProfileForm(request.POST, instance=profile)

        if profileform.is_valid():
            print(profileform)
            #new_val = form.save(commit=False)
            profile = profileform.save(commit=False)
            profile.bmi = profile.weight/(profile.height*0.01*profile.height*0.01)
            profile.save()

            new_profile_val = Profile.objects.get(user=request.user).as_dict()

            new_weight.user = request.user
            new_weight.date = datetime.date.today()
            new_weight.weight = profile.weight
            new_weight.save()

            new_bodystats.user = request.user
            new_bodystats.date = datetime.date.today()
            new_bodystats.bone = profile.bone
            new_bodystats.muscle = profile.muscle
            new_bodystats.water = profile.water
            new_bodystats.fat = profile.fat
            new_bodystats.bmi = profile.weight/(profile.height*profile.height)
            new_bodystats.save()
            return redirect('profile')

    else:
        profileform = ProfileForm(instance=profile)
        profileform.picture = profile.picture
        print(profileform.picture)
    return render(request, 'userprofile/modifyProfile.html', {"profileform": profileform, "profile": profile})