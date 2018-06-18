from django.shortcuts import render, _get_queryset
from django.http import HttpResponse
from django.template import loader, Context, Template
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from .forms import WorkoutForm, RoutineForm

#importing own classes
from .models import Equipment, Routine, Workout, User

@login_required
def index(request):

    try:
        workout = Workout.objects.get(user=request.user).as_dict()
    except:
        return render(request, 'training/training.html',
                      {
                          "error": "Kein Trainingsplan vorhanden! Melde dich bei einem Trainer, um einen zu erstellen."
                      })
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
