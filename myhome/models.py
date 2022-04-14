from ast import mod
from distutils.command.upload import upload
from tkinter import CASCADE
from turtle import mode
from django.db import models

# Create your models here.

class TourPackage(models.Model):
    tour_name = models.CharField(max_length=255)
    package_price = models.IntegerField(default=0)
    picture = models.ImageField(upload_to="tourImages", null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tour_name}"


class VisitPlaces(models.Model):
    package = models.ForeignKey(TourPackage, on_delete=models.CASCADE, null=True)
    place_name=models.CharField(max_length=200)
    picture = models.ImageField(upload_to="placeImages", null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return f"{self.place_name}"