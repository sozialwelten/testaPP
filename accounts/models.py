from django.db import models

from testapp.settings import DOMAIN

# Create your models here.
class Account(models.Model):
    handle = models.CharField(max_length = 30, blank = False, null = False)
    name = models.CharField(max_length = 30, blank = False, null = False)

    def __str__(self):
        return f"{ self.name }@{ self.handle }@{ DOMAIN }"

    def __repr__(self):
        return f"[accounts/Account]{ self.name }(at){ self.handle }(at){ DOMAIN }"
