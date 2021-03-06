from django import forms
from .models import Workout, Routine

class WorkoutForm(forms.ModelForm):

    class Meta:
        model = Workout
        fields = ("name",)

class RoutineForm(forms.ModelForm):

    class Meta:
        model = Routine
        fields = ("name",)