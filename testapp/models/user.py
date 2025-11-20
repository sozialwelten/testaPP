from django.db import models

import testapp as ta
from testapp.utils.presets import *


class UserAccounts(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True, unique=True)

    # with 'display_name@username@instance.ext'
    username = models.CharField(max_length=CHARFIELD_LEN_M, unique=True)
    display_name = models.CharField(max_length=CHARFIELD_LEN_M)         

    def __str__(self):
        return f"@{self.username}"

    @property
    def accounthandle(self) -> str:
        return f"{self.username}@{ta.settings.DOMAIN}"

    @property
    def page(self) -> str:
        return f"https://{ta.settings.DOMAIN}@{self.username}"


class UserToken(models.Model):
    ...

class Route(models.Model):
    ...

