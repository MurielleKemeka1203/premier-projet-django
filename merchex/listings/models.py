from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Band(models.Model):
    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'

    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(max_length=50)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(
    validators=[MinValueValidator(1900), MaxValueValidator(2021)])
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)
    genre = models.fields.CharField(choices=genre.choices, max_length=5)

    def __str__(self):
        return f'{self.name}'


    
class Listings(models.Model):

    class ListingsType(models.TextChoices):
        RECORDS = 'R'
        CLOTHING = 'C'
        POSTERS = 'P'
        MISC = 'M'

    title = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=1000)
    sold = models.fields.BooleanField(default=False)
    year = models.fields.IntegerField(
        null=True,
         validators=[MinValueValidator(1900), 
                    MaxValueValidator(2021)]
    )

    type = models.fields.CharField(choices=ListingsType.choices, max_length=5)
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)




