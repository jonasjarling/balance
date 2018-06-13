from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.BigAutoField
    joined = User.date_joined
    dateOfBirth = models.DateField
    adress = models.CharField(max_length=50, blank=True)
    email = User.email
    telephone = models.CharField(max_length=20, blank=True)
    sex = models.BooleanField('f','m')
    height = models.IntegerField
    weight = models.IntegerField