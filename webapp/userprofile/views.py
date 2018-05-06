from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse


@login_required
def userprofile(request):
    context = {
        'test': '123'
    }
    return render(request, 'userprofile/profile.html', context)