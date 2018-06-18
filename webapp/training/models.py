from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Equipment(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

    def as_dict(self):
        return {
            "name": self.name,
            "number": self.number
        }


class Routine(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    setup = models.CharField(max_length=200, blank=True, null=True)
    reps = models.IntegerField(default=0)
    sets = models.IntegerField(default=0)
    description = models.CharField(max_length=500, blank=True, null=True)
    equipment = models.ForeignKey(Equipment, blank=True, null=True, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='training/', height_field=None, width_field=None, max_length=100, blank=True,
                                null=True)

    def as_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "setup": self.setup,
            "reps": self.reps,
            "sets": self.sets,
            "equipment": self.equipment,
            "picture": self.picture.url
        }

    def __str__(self):
        return self.name


class Workout(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    createdBy = models.CharField(max_length=50, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    routine = models.ManyToManyField(Routine, blank=True, null=True)
    progress = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def as_dict(self):
        return {
            "name": self.name,
            "createdBy": self.createdBy,
            "user": self.user,
            "routine": self.routine.values(),
            "progress": self.progress
        }