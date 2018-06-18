from django import forms
from .models import User, Profile, BodyStats, Weight

class WeightForm(forms.ModelForm):
    #user = Weight.user
    #date = Weight.date
    #weight = Weight.weight
    class Meta:
        model = Weight
        fields = ('weight',)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('picture', 'height', 'weight', 'fat', 'muscle', 'bone', 'water',)

class WaageForms(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('height', 'weight', 'fat', 'muscle', 'bone', 'water',)