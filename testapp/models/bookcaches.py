from django.db import models
from enum import Enum


### CONSTANTS ###
_geo_max_decimals = 4

class AccessLevels(str, Enum):
    HIDDEN = "unsichtbar"
    PRIVATE = "privat"
    PUBLIC = "öffentlich"

class BookCacheType(str, Enum):
    BOOKCASE = "Bücherschrank"
    LIBRARY = "Bibliothek"
    COLLECTION = "Sammlung"
    ARCHIVE = "Archiv"
    DIGITAL = "Digital"


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



class BookCaches(models.Model):
    """Models for any type of "book cache", mainly "PublicBookcases".
    """
    id = models.IntegerField(primary_key = True, unique = True, auto_created = True)
    access_level = models.CharField(choices = [(k, v) for k,v in AccessLevels], default = "PRIVATE")

    location = models.ForeignKey(
        GeoLocations,
        on_delete = models.CASCADE,
        related_name = "bookcaches",
        unique = True,
        db_index = True,
    )

    def __str__(self):
        return str(self.id)
