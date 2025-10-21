from django.db import models

# Create your models here.
class BibKey(models.Model):
    series = models.CharField(max_length = 4)
    user = models.CharField()
    

