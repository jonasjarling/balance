from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.


class Weight(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    weight = models.FloatField(blank=True)

    def __str__(self):
        return "%s %s" % (self.user, self.date)

    def as_dict(self):
        return {
            str(self.id): {
                "date": self.date,
                "weight": self.weight,
            },
        }


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dateOfBirth = models.DateField(blank=True, null=True)
    adress = models.CharField(max_length=50, blank=True)
    telephone = models.CharField(max_length=20, blank=True)
    sex = models.CharField(max_length=10, null=True, blank=True)
    height = models.IntegerField(blank=True, null=True)
    goal = models.CharField(max_length=500, blank=True, null=True)
    picture = models.ImageField(upload_to="profilePics/", height_field=None, width_field=None, max_length=100, blank=True, null=True)

    weight = models.FloatField(blank=True, null=True)
    fat = models.FloatField(blank=True, null=True)
    muscle = models.FloatField(blank=True, null=True)
    bone = models.FloatField(blank=True, null=True)
    water = models.FloatField(blank=True, null=True)
    bmi = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.user.username

    def as_dict(self):
        return{
            "id":self.user.id,
            "first_name":self.user.first_name,
            "last_name":self.user.last_name,
            "last_login":self.user.last_login,
            "date_joined":self.user.date_joined.date(),
            "dateOfBirth":self.dateOfBirth,
            "adress":self.adress,
            "email":self.user.email,
            "telephone":self.telephone,
            "sex":self.sex,
            "height":self.height,
            "goal":self.goal,
            "picture":self.picture.url,
            "weight":self.weight,
            "fat":self.fat,
            "muscle":self.muscle,
            "bone":self.bone,
            "water":self.water,
            "bmi":self.bmi,
        }


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwags):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwags):
    instance.profile.save()
