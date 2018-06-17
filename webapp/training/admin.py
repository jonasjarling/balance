from django.contrib import admin
from .models import Equipment, Workout, Routine
# Register your models here.

admin.site.register(Equipment)
admin.site.register(Workout)
admin.site.register(Routine)
