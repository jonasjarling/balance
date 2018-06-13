from django.contrib import admin
from .models import Exercise, Equipment, Trainingplan
# Register your models here.

admin.site.register(Exercise)
admin.site.register(Equipment)
admin.site.register(Trainingplan)
