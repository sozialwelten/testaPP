from django.db import models

from .utils import COUNTRY_CODES, get_country_name

# Create your models here.
class Location(models.Model):
    lat = models.DecimalField(
        verbose_name = "Latitude",
        decimal_places = 4,
        blank = False, null = False
    )
    lon = models.DecimalField(
        verbose_name = "Longitude",
        decimal_places = 4,
        blank = False, null = False
    )
    class Meta:
        constraints = [ models.UniqueConstraint(fields = ["lon", "lat"], name = "point") ]

class Address(models.Model):
    street = models.CharField(max_length = 30, blank = True, null = False)
    number = models.CharField("street number", max_length = 30, blank = True, null = True)
    city = models.CharField(max_length = 30)
    region = models.CharField(max_length = 30)

    postcode = models.IntegerField(max_length = 30, blank = True, null = True)
    country_code = models.Choices(str, names = COUNTRY_CODES)

    comment = models.CharField(max_length = 255, blank = True, null = True)

    class Meta:
        constraints = [ models.UniqueConstraint(fields = [
            "country_code", "region", "city" , 
            "postcode", "street", "number"
        ], name = "address") ]

class BookCache(models.Model):
    loc = models.OneToOneField(Location, on_delete = models.CASCADE, related_name = "bookcache")
    address = models.OneToOneField(Location, on_delete = models.CASCADE, related_name = "bookcache")
    directions = models.CharField(max_length = 255, blank = True, null = True)
