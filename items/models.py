from django.db import models
from django.contrib.postgres.fields import JSONField, ArrayField

class Person(models.Model):
    name = models.CharField(max_length = 32, null = False, blank = False)
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

class BookItem(models.Model):
    title = models.CharField(max_length = 32)
    subtitle = models.CharField(max_length = 32, default = None)
    publisher = models.CharField(max_length = 32, default = None)
    year = models.IntegerField(max_length = 4, default = None)
    agent = models.ForeignKey(Person, on_delete = models.CASCADE, related_name = "books")

class UniqueID(models.Model):
    library = models.CharField(max_length = 255, default = "~")

    series = models.IntegerField(max_length = 4, default = 0)
    token = models.CharField(max_length = 6, blank = False, null = False)
    id = models.CharField(max_length = 3)
    id_suffix = models.CharField(max_length = 64)

    book = models.ForeignKey(BookItem, on_delete = models.CASCADE, related_name = "signature")

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields = ["library", "series", "token", ],
                name = "unique_key"
            ),
        ]

    def __str__(self) -> str:
        result = f"[{ self.library.lower() }]{ self.series:num04 }{ self.token.upper() }{ self.id:num03 }"
        if self.id_suffix:
            result += f"-{ self.id_suffix.lower() }"
        return result
