from django.shortcuts import render

from django.http import HttpResponse

def statistic(request):
    context = {
        'test': '123'
    }
    return render(request, 'statistic/statistic.html', context)