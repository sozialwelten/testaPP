from datetime import datetime as dt
from django.db import models
from django.contrib.postgres.fields import ArrayField
from enum import Enum

import testapp as ta
from testapp.models.base import TaBaseModel
from testapp.models.user import UserAccount
from testapp.utils.presets import *

class CacheAccess(Enum):
    HIDDEN = -1 
    BLOCKED = 0
    PRIVATE = 1 
    MODERATED = 2 
    PUBLIC = 3 

class BookCaches(TaBaseModel):
    """Models for any type of "book cache", mainly "PublicBookcases".
    """
    owner = models.ForeignKey(UserAccount,
                              on_delete=models.CASCADE,
                              related_name="BookCaches",
                              unique=True,
                              help_text="The user account having control over this bookcache. If 'Null' defaults to instance.",
                              default=ta.settings.DOMAIN,
                              )
    long = models.DecimalField(decimal_places=MAX_GEO_DECIMALS)
    lat = models.DecimalField(decimal_places=MAX_GEO_DECIMALS)
    mods = ArrayField(models.CharField(max_length=CHARFIELD_LEN_M))
    access_rules = models.CharField(max_length=CHARFIELD_LEN_M)

    links_listen = ArrayField(models.CharField(max_length=CHARFIELD_LEN_X))
    links_inform = ArrayField(models.CharField(max_length=CHARFIELD_LEN_X))
    followers = ArrayField(models.CharField(max_length=CHARFIELD_LEN_X))

    def __str__(self):
        base = f"bc#{self.id}"
        if self.owner == ta.settings.DOMAIN:
            return f"{base}@{ta.settings.DOMAIN}"
        else:
            return f"{base}{self.owner.accounthandle}"

    def locate(self) -> tuple[int, int]:
        return (self.lat, self.long)
        


class CmtNotes(TaBaseModel):
    owner = models.ForeignKey(BookCaches,
                              on_delete = models.CASCADE,
                              related_name = "Notes")
    author = models.CharField(max_length=64)
    timestamp = models.CharField(max_length=24)
    content = models.CharField(max_length=355)

    def __str__(self):
        return self.id

    def __eq__(self, other) -> bool:
        if isinstance(other, dt):
            return dt.fromisoformat(self.timestamp) == other
        elif isinstance(other, str):
            return self.timestamp == other
        elif isinstance(other, CmtNotes):
            return self.timestamp == other.timestamp
        else:
            return False

    def short(self, max: int = 15) -> str:
        return ta.fn.limit_text(limit=max, text=self.content)
