from django.db import models

class GeoData(models.Model):
    latitude = models.DecimalField(decimal_places = 4, blank = False, null = False)
    class Meta:
        constraints = [ models.UniqueConstraint(fields = ["lon", "lat"], name = "Point") ]

CACHE_ACCESS_LEVELS: list[tuple] = [
    ("HIDDEN", "HIDDEN"),
    ("PRIVATE", "PRIVATE"),
    ("PUBLIC", "PUBLIC")
]
class Bookcache(models.Model):
    access = models.CharField(choices = CACHE_ACCESS_LEVELS, default = "PRIVATE")
