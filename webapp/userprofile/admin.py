from django.contrib import admin
from .models import Profile, Weight, BodyStats
# Register your models here.


admin.site.register(Profile)
admin.site.register(Weight)
admin.site.register(BodyStats)