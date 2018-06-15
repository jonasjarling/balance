from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Equipment(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name


class Exercise(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    equipment = models.ManyToManyField(Equipment, blank=True)
    picture = models.ImageField(upload_to='training/', height_field=None, width_field=None, max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

    def exercise_as_dict(self):
        return {
            str(self.id): {
                "name": self.name,
                "description": self.description,
                "equipment": self.equipment,
                "picture": self.picture
            }
        }


class Workout(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    createdBy = models.CharField(max_length=50, blank=True, null=True)
    user = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.name


class Routine(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    exercise = models.ManyToManyField(Exercise, blank=True)
    workout = models.ManyToManyField(Workout, blank=True)
    setup = models.CharField(max_length=200, blank=True, null=True)
    reps = models.IntegerField(default=0)
    sets = models.IntegerField(default=0)

    def __str__(self):
        return self.name
