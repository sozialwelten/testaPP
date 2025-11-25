from datetime import datetime as dt
from django.db import models
from django.contrib.postgres.fields import ArrayField
from enum import Enum

import testapp as ta
from testapp.models.base import TaBaseModel
from testapp.models.user import User
from testapp.utils.presets import *

class AccessLevel(models.TextChoices):
    PRIVATE = "private", "private"
    EXPLICIT = "moderated", "requestable"
    LIMITED = "limited", "only-for-instance"
    PUBLIC = "public", 'public'

class Library(TaBaseModel):
    # Location 
    long = models.DecimalField(decimal_places=GEO_DEC_MAX)
    lat = models.DecimalField(decimal_places=GEO_DEC_MAX)

    # Maintainers, if any
    owner = models.ForeignKey(
        User,
        related_name="BookCaches",
        unique=True,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        help_text="User maintaining and/or owning this library",
    )
    mods = ArrayField(models.CharField(max_length=CHAR_LEN_M), null=True, blank=True)

    # Access rules
    viz_access = models.CharField(choices=AccessLevel.choices, max_length=CHAR_LEN_M, null=False, blank=True, default=AccessLevel.PUBLIC)
    contrib_access = models.CharField(choices=AccessLevel.choices, max_length=CHAR_LEN_M, null=False, blank=True, default=AccessLevel.PUBLIC)
    stock_access = models.CharField(choices=AccessLevel.choices, max_length=CHAR_LEN_M, blank=True, null=False, default=AccessLevel.LIMITED)

    def __str__(self) -> str:
        return getattr(self, 'name', f"bib")

    def locate(self) -> tuple[int, int]:
        return (self.lat, self.long)
        

class CmtNotes(TaBaseModel):
    owner = models.ForeignKey(Library,
                              on_delete = models.CASCADE,
                              related_name = "Notes")
    author = models.CharField(max_length=64)
    timestamp = models.CharField(max_length=24)
    content = models.CharField(max_length=355)
