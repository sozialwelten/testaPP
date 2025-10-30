from django.db import models
from typing import Literal

from testapp.settings import BASE_URL
from testapp.utils.helpers import HttpUrl 

class ActivityPubMixin(models.Model):
    _owner: str|None = None
    _name = models.CharField(max_length = 50, blank = False, null = False) 

    def get_local_name(self, _base: str = BASE_URL) -> HttpUrl:
        result = HttpUrl(getattr(self, "_owner", BASE_URL))
        result.update(
            self.__class__.__name__.upper(),
            getattr(self, "name")
        )
        return result

