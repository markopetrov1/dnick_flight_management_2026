from django import forms

from baloons.models import  Flight


# class FlightForm(forms.Form):
#     code = forms.CharField(max_length=255)
#     airport_from = forms.CharField(max_length=255)
#     airport_to = forms.CharField(max_length=255)
#     photo = forms.ImageField()
#     pilot = forms.ModelChoiceField(queryset=Pilot.objects.all())

class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        # fields =
        exclude = ['user',]