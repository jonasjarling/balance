from django.db import models

# Create your models here.


class Trainingplan(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Equipment(models.Model):
    name = models.CharField(max_length=50)
    number = models.IntegerField()

    def __str__(self):
        return self.name

class Exercise(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    equipment = models.OneToOneField(Equipment, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='uploads/', height_field=None, width_field=None, max_length=100)

    def __str__(self):
        return self.name


