from django.shortcuts import render

from django.http import HttpResponse

def userprofile(request):
    context = {
        'test': '123'
    }
    return render(request, 'userprofile/profile.html', context)