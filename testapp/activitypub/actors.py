from django.db import models

from testapp.settings import DOMAIN

class ActivityPubActor(models.Model):
    name = models.CharField(max_length = 50)
    ap_type = models.CharField(max_length = 50)

    link_type_par: str|None = None
    link_field_par: str|None = None
