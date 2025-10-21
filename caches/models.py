from django.db import models
from django_countries.fields import CountryField

GEO_DECIMAL_PLACES = 4 # ca. 11m

# Create your models here.
class BookCache(models.Model):
    lat = models.DecimalField("latitude", decimal_places = GEO_DECIMAL_PLACES) 
    long = models.DecimalField("longitude", decimal_places = GEO_DECIMAL_PLACES)

    country = CountryField()
    region = models.CharField()
    city = models.CharField()
    street = models.CharField()

    owner = models.CharField()
    maintainer = models.CharField()

    cache_type = models.Choices(names = [""])
