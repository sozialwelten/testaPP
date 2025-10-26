from django.db import models

from .utils import COUNTRY_CODES, get_country_name

from items.models import Book

# Create your models here.
class GeoData(models.Model):
    latitude = models.DecimalField(decimal_places = 4, blank = False, null = False)
    class Meta:
        constraints = [ models.UniqueConstraint(fields = ["lon", "lat"], name = "Point") ]


class BookCache(models.Model):
    location = models.OneToOneField(GeoData, on_delete = models.CASCADE, related_name = "bookcache")
    stock = models.ManyToManyField(Book, )
