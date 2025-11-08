from django.db import models
from django.contrib.postgres.fields import ArrayField, JSONField
from enum import Enum
from sys import exit

import testapp as ta


### CONSTANTS ###
_geo_max_decimals = 4

class GeoLocations(models.Model):
    latitude = models.DecimalField(
        decimal_places = _geo_max_decimals,
        blank = False,
        null = False
    )
    longitude = models.DecimalField(
        decimal_places = _geo_max_decimals,
        blank = False,
        null = False
    )
    class Meta:
        constraints = [ models.UniqueConstraint(fields = ["lon", "lat"], name = "Point") ]

class CacheAccess(Enum):
    HIDDEN = -1 
    BLOCKED = 0
    PRIVATE = 1 
    MODERATED = 2 
    PUBLIC = 3 

class BookCaches(models.Model):
    """Models for any type of "book cache", mainly "PublicBookcases".
    """
    id = models.IntegerField(primary_key = True, unique = True, auto_created = True)
    owner = models.CharField(max_length = 32)

    mods = ArrayField(models.CharField(max_length=32))
    access_rules = models.CharField(max_length=64)

    links_receive = ArrayField(models.CharField(max_length=64))
    links_send = ArrayField(models.CharField(max_length=64))

    followers = ArrayField(models.CharField(max_length=64))

    location = models.ForeignKey(
        GeoLocations,
        on_delete = models.CASCADE,
        related_name = "bookcaches",
        unique = True,
        db_index = True,
    )
    def __str__(self):
        return str(self.id)
