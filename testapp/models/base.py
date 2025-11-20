from datetime import datetime as dt
from django.db import models

import testapp as ta
from testapp.utils.presets import *


# --- BASE MODEL ---
# basic repeatable functionalities
class TaBaseModel(models.Model):
    id = models.IntegerField(primary_key=True,
                             auto_created=True,
                             unique=True,
                             null=False)
    created_at = models.DateTimeField(auto_now_add=True,)
    updated_at = models.DateTimeField(auto_now_add=True)

    group = models.CharField(max_length=CHARFIELD_LEN_S,
                                       null=True,
                                       unique=False,
                                       choices=[(n, v) for n, v in PageGroupNames])
    class Meta:
        abstract = True

    def get_local_address(self) -> str:
        owner: TaBaseModel|None = getattr(self, 'owner', None)
        if owner:
            prefix = owner.get_local_address()
        else:
            prefix = ta.settings.DOMAIN

        if self.group:
            prefix += f"/{self.group.upper()}"
        return f"{prefix}/{self}"
