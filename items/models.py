from django.db import models
from django.contrib.postgres.fields import JSONField
import re

from accounts.models import UserToken
from testapp.utils.schemes import Eigenname

class Person(models.Model):
    name = models.CharField(max_length = 255, null = False, blank = False)
    birth = models.IntegerField(max_length = 4, null = True, blank = True)
    death = models.IntegerField(max_length = 4, null = True, blank = True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields = ["library", "series", "token", ],
                name = "unique_reference"
            ),
        ]

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"[items/person]{ self.name }({ self.birth or "?" }-{ self.death or "?" })"

class Book(models.Model):
    title = models.CharField(max_length = 32, blank = False, null = False)
    subtitle = models.CharField(max_length = 32, default = None)
    author = models.ManyToManyField(Person, related_name = "books")
    editor = models.ManyToManyField(Person, related_name = "books")
    translator = models.ManyToManyField(Person, related_name = "books")
    editors = models.JSONField()

    year = models.IntegerField(max_length = 4, null = True, blank = True)
    location = models.CharField(max_length = 30, null = True, blank = True)
    publisher = models.CharField(max_length = 32, default = None)

    year = models.IntegerField(max_length = 4, default = None)

    def __str__(self):
        if self.year:
            return f"{ self.title } ({ self.year })"
        return self.title




class Signature(models.Model):
    library = models.CharField(max_length = 255, default = "~")
    token = models.ForeignKey(UserToken, on_delete = models.CASCADE, related_name = "entries")
    series = models.IntegerField(max_length = 4, default = 0)
    index = models.CharField(max_length = 3)
    suffix = models.CharField(max_length = 30)
    book = models.ForeignKey(Book, on_delete = models.CASCADE, related_name = "signatures")

    class Meta:
        constraints = [
            models.UniqueConstraint(fields = ["library", "series", "token", "group", "item" ], name = "unique_key"),
        ]

    def __str__(self) -> str:
        result = f"[{ self.library.lower() }]{ self.series:num04 }{ self.token }{ self.index }"

        if self.suffix:
            result += f"-{ self.suffix }"
        return result
