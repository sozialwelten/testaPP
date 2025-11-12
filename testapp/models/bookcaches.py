from datetime import datetime as dt
from django.db import models
from django.contrib.postgres.fields import ArrayField
from enum import Enum

import testapp as ta


### CONSTANTS ###
_geo_max_decimals = 4

class CacheAccess(Enum):
    HIDDEN = -1 
    BLOCKED = 0
    PRIVATE = 1 
    MODERATED = 2 
    PUBLIC = 3 

class BookCaches(models.Model):
    """Models for any type of "book cache", mainly "PublicBookcases".
    """
    id = models.IntegerField(primary_key = True,
                             unique = True,
                             auto_created = True
                             )
    long = models.DecimalField(decimal_places = 4)
    lat = models.DecimalField(decimal_places = 4)
    owner = models.CharField(max_length = 32)
    mods = ArrayField(models.CharField(max_length=32))
    access_rules = models.CharField(max_length=64)

    links_listen = ArrayField(models.CharField(max_length=64))
    links_inform = ArrayField(models.CharField(max_length=64))
    followers = ArrayField(models.CharField(max_length=64))

    def __str__(self):
        return str(self.id)
    
    def locate(self) -> tuple[int, int]:
        return (self.lat, self.long)
        



class Comments(models.Model):
    FORMAT = "%Y-%m-%dT%H:%M:%S.%s%z"
    id = models.IntegerField(primary_key = True,
                             unique = True,
                             auto_created = True,)
    owner = models.ForeignKey(BookCaches,
                              on_delete = models.CASCADE,
                              related_name = "Comments")
    author = models.CharField(max_length=64)
    timestamp = models.CharField(max_length=24)
    content = models.CharField(max_length=355)

    def __str__(self):
        return f"{self.timestamp}\t{self.content}\nby {self.author}"

    def __eq__(self, other) -> bool:
        """Timestamp comparison. Can be string time (see Comment.FORMAT), datetime object or Comment.
        """
        if isinstance(other, dt):
            return dt.fromisoformat(self.timestamp) == other
        elif isinstance(other, str):
            return self.timestamp == other
        elif isinstance(other, Comments):
            return self.timestamp == other.timestamp
        else:
            return False

    def short(self, max: int = 15) -> str:
        return ta.fn.limit_text(limit=max, text=self.content)


