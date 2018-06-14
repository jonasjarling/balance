from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Equipment(models.Model):
    name = models.CharField(max_length=50)
    number = models.IntegerField()

    def __str__(self):
        return self.name


class Exercise(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    equipment = models.ManyToManyField(Equipment)
    picture = models.ImageField(upload_to='training/', height_field=None, width_field=None, max_length=100)

    def __str__(self):
        return self.name


class Workout(models.Model):
    name = models.CharField(max_length=50)
    createdBy = models.CharField(max_length=50)
    user = models.ManyToManyField(User)

    def __str__(self):
        return self.name


class Routine(models.Model):
    name = models.CharField(max_length=100)
    exercise = models.ManyToManyField(Exercise)
    workout = models.ManyToManyField(Workout)
    setup = models.CharField(max_length=200)
    reps = models.IntegerField()
    sets = models.IntegerField()

    def __str__(self):
        return self.name
