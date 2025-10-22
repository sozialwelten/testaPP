from django.db import models

# Create your models here.
class Library(models.Model):
    timestamp = models.DateTimeField()
    name = models.CharField(max_length = 255)

    def __eq__(self, other):
        if isinstance(other, Library):
            return other.name == self.name and other.timestamp == self.timestamp
        return False
