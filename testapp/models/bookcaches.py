from django.db import models

from testapp.models.base import ActivityPubMixin

GEODATA_MAX_DECIMALS = 4        # So area for identifying object is not to narrow

def hello(world) -> str:
    return "hello"

what = [1, 2, 3]

x = 2 + 3 * 4 -2

class GeoLocations(models.Model):
    latitude = models.DecimalField(
        decimal_places = GEODATA_MAX_DECIMALS,
        blank = False,
        null = False
    )
    longitude = models.DecimalField(
        decimal_places = GEODATA_MAX_DECIMALS,
        blank = False,
        null = False
    )
    class Meta:
        constraints = [ models.UniqueConstraint(fields = ["lon", "lat"], name = "Point") ]




CACHE_ACCESS_LEVELS: list[tuple] = [
    ("HIDDEN", "HIDDEN"),
    ("PRIVATE", "PRIVATE"),
    ("PUBLIC", "PUBLIC")
]
class BookCaches(models.Model, ActivityPubMixin):
    id = models.IntegerField(primary_key = True, unique = True, auto_created = True)
    access_level = models.CharField(choices = CACHE_ACCESS_LEVELS, default = "PRIVATE")
    location = models.ForeignKey(
        GeoLocations,
        on_delete = models.CASCADE,
        related_name = "bookcache",
        unique = True,
        db_index = True,
    )

    def __str__(self):
        return str(self.id)

    @property
    def name(self) -> str:
        return f"bc{self.id}"
