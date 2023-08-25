from django.db import models
from django.core.validators import MaxValueValidator
from users.models import CustomUser
from datetime import datetime

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=255, blank=False)
    serves = models.IntegerField(blank=False, validators=[MaxValueValidator(200)])
    tags = models.JSONField(blank=True, default=None)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateField(default=datetime.now())


class Ingredient(models.Model):
    name = models.CharField(max_length=255, blank=False)
    
    CUPS = "Cups",
    TABLESPOON = "TBSP",
    TEASPOON = "TSP",
    OUNCE = "Oz",
    POUNDS = "Lbs",
    GALLON = "gal",
    EACH = "ea",
    GRAM = "g",
    MILLIGRAM = "mg",
    KILOGRAM = "kg",

    units = (
        (CUPS,"Cups"),
        (TABLESPOON,"TBSP"),
        (TEASPOON,"TSP"),
        (OUNCE,"Oz"),
        (POUNDS,"Lbs"),
        (GALLON,"gal"),
        (EACH,"ea"),
        (GRAM,"g"),
        (MILLIGRAM,"mg"),
        (KILOGRAM,"kg"),
    )

    unit = models.CharField(max_length=50, choices=units, default=EACH)
    quantity = models.IntegerField(blank=False, validators=[MaxValueValidator(254)])
    in_stock = models.BooleanField(default=False)


class Steps(models.Model):
    step_number = models.IntegerField(blank=False, validators=[MaxValueValidator(254)])
    step_text = models.TextField(blank=False)
    is_complete = models.BooleanField(default=False)
