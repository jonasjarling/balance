from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Context, Template
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

#importing own classes
from .models import Equipment, Routine, Workout, User

@login_required
def index(request):
    #context = [obj.get_context() for obj in Routine.objects.all()]
    workout = Workout.objects.get(user=request.user).as_dict()

    routines = Routine.objects.get_queryset().filter(workout__user=request.user)
    routine = {}
    for obj in routines:
        routine[obj] = obj.as_dict()

    equipment = Equipment.objects.filter(routine__workout__user=request.user).values()

    return render(
        request,
        'training/training.html',
        {
            "workout": workout,
            "routine": routine.values(),
            "equipment": equipment.values()
        }
    )

def plan(request, plan_id):

    template = loader.get_template('training/index.html')
    context = {
        "plan":{
            "id":"1",
            "name":"fett pumpen",
            "exercise":{
                "id":"123",
                "image":"http://img.pr0gramm.com/2018/03/05/0ea61924c23f153c.jpg",
                "repeat":"6",
                "weight":"42",
            },
            "exercise": {
                "id": "124",
                "image": "http://img.pr0gramm.com/2018/03/05/0ea61924c23f153c.jpg",
                "repeat": "62",
                "weight": "45",
            },
            "exercise": {
                "id": "125",
                "image": "http://img.pr0gramm.com/2018/03/05/0ea61924c23f153c.jpg",
                "repeat": "37",
                "weight": "69",
            },
        },
        "plan": {
            "id": "2",
            "name":"disco pumpen",
            "exercise": {
                "id": "1",
                "image": "http://img.pr0gramm.com/2018/03/05/0ea61924c23f153c.jpg",
                "repeat": "6",
                "weight": "42",
            },
            "exercise": {
                "id": "12",
                "image": "http://img.pr0gramm.com/2018/03/05/0ea61924c23f153c.jpg",
                "repeat": "62",
                "weight": "45",
            },
            "exercise": {
                "id": "3",
                "image": "http://img.pr0gramm.com/2018/03/05/0ea61924c23f153c.jpg",
                "repeat": "37",
                "weight": "69",
            },
        },
    }
    return render(request, "training/training.html", context)
    #return HttpResponse(t,emplate.render(context)) #request