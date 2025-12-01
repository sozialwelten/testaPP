from datetime import datetime as dt
from django.db import models
from django.contrib.postgres.fields import ArrayField

import testapp as ta
from testapp.utils.presets import *
from testapp.utils.schemes import *


# --- BASE MODEL ---
class TaBaseModel(models.Model):
    id = models.AutoField(
        primary_key=True,
        auto_created=True,
        unique=True,
        null=False
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class ActivityPubBaseModel(models.Model):

    class Meta:
        abstract = True

    def get_local_name(self) -> str:
        link = [ta.settings.DOMAIN]

        if hasattr(self, 'owner'):
            link = [getattr(self, 'owner').get_local_name()]

        # if library...
        if hasattr(self, 'long') and hasattr(self, 'lat'):
            link += ['BIB', getattr(self, 'long'), getattr(self, 'lat')]

        # if book...
        elif hasattr(self, 'title'):
            if hasattr(self, 'owner'):
                link += ['BOOK', getattr(self, 'stamp')]
            elif hasattr(self, 'author'):
                link += ['BOOK', getattr(self, 'author'), getattr(self, 'title')]
            else:
                link += ['BOOK', getattr(self, 'title')] 

        # if account...
        elif hasattr(self, 'username'):
            link += [getattr(self, 'username')]
        # if document or document like
        elif hasattr(self, 'doctype'):
            link += [
                getattr(self, 'doctype','doc').upper(),
                getattr(self, 'name',getattr(self, 'id'))
            ]
        else:
            link += [getattr(self, 'name', getattr(self, 'id'))]
        return "/".join(link)


class ActivityPubActor(models.Model):
    follows = ArrayField(
        models.CharField(max_length=CHAR_LEN_X),
        blank=True,
        null=True
    )
    followed_by = ArrayField(
        models.CharField(max_length=CHAR_LEN_X),
        blank=True,
        null=True,
    )

    class Meta:
        abstract = True
