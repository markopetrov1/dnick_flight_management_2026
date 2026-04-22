from django.contrib.auth.models import User
from django.db import models

class Flight(models.Model):
    code = models.CharField(null=False, blank=False, max_length=255, unique=True)
    airport_from = models.CharField(max_length=255)
    airport_to = models.CharField(max_length=255)
    baloon_information = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="photos/")
    pilot = models.ForeignKey("Pilot", on_delete=models.CASCADE)
    airline = models.ForeignKey("Airline", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'Flight {self.code} - {self.airline} '

class Pilot(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    year_of_birth = models.IntegerField()
    total_hours_of_flight = models.IntegerField()
    rank = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} {self.surname}'

class Baloon(models.Model):
    TYPES = [
        ("type1", "Type 1"),
        ("type2", "Type 2"),
        ("type3", "Type 3"),
    ]
    type = models.CharField(choices=TYPES)
    manufacturer = models.CharField(max_length=255)
    max_num_passengers = models.IntegerField()

    def __str__(self):
        return f'{self.type} - {self.manufacturer}'


class Airline(models.Model):
    name = models.CharField(max_length=255)
    year_of_establishment = models.CharField(max_length=255)
    num_planes = models.IntegerField(null=True, blank=True)
    outside_EU = models.BooleanField(default=False)

    def __str__(self):
        return self.name