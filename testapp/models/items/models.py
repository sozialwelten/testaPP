from django.db import models
from django.contrib.postgres.fields import ArrayField

from accounts.models import UserToken

class Book(models.Model):
    title = models.CharField(max_length = 30, blank = False, null = False)
    year = models.IntegerField(max_length = 4, null = True, blank = True)
    author = ArrayField(models.CharField(max_length = 30))
    editor = ArrayField(models.CharField(max_length = 30))

    subtitle = models.CharField(max_length = 30, default = None)

    translator = ArrayField(models.CharField(max_length = 30))
    illustrator = ArrayField

    rest = models.JSONField("other")

    location = models.CharField(max_length = 30, null = True, blank = True)
    publisher = models.CharField(max_length = 32, default = None)

    year = models.IntegerField(max_length = 4, default = None)

    def __str__(self):
        if self.year:
            return f"{ self.title } ({ self.year })"
        return self.title

#class Signature(models.Model):
#    library = models.CharField(max_length = 255, default = "~")
#    token = models.ForeignKey(UserToken, on_delete = models.CASCADE, related_name = "entries")
#    series = models.IntegerField(max_length = 4, default = 0)
#    index = models.CharField(max_length = 3)
#    suffix = models.CharField(max_length = 30)
#    book = models.ForeignKey(Book, on_delete = models.CASCADE, related_name = "signatures")
#
#    class Meta:
#        constraints = [
#            models.UniqueConstraint(fields = ["library", "series", "token", "group", "item" ], name = "unique_key"),
#        ]
#
#    def __str__(self) -> str:
#        result = f"[{ self.library.lower() }]{ self.series:num04 }{ self.token }{ self.index }"
#
#        if self.suffix:
#            result += f"-{ self.suffix }"
#        return result
