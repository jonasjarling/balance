from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    joined = User.date_joined
    dateOfBirth = models.DateField
    adress = models.CharField(max_length=50, blank=True)
    email = User.email
    telephone = models.CharField(max_length=20, blank=True)
    sex = models.CharField(max_length=10)
    height = models.IntegerField
    goal = models.CharField(max_length=500)
    picture = models.ImageField(upload_to="profilePics/", height_field=None, width_field=None, max_length=100)

    weight = models.IntegerField
    fat = models.FloatField
    muscle = models.FloatField
    bone = models.FloatField
    water = models.FloatField
    bmi = models.FloatField

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwags):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwags):
    instance.profile.save()
