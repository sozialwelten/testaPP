from django.db import models
from django.contrib.auth.models import User

import testapp as ta
from testapp.utils.presets import *

# Django itself creates a user profile, that we will append here to implement custom 
# behaviour/fields and connect user profile to ActivityPub implementation

class UserProfile(models.Model):
    id = models.IntegerField(primary_key = True)

    # Django user, carries username and password
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name="profile")

    # with 'display_name@User.username@instance.ext'
    display_name = models.CharField(max_length=CHAR_LEN_M)

    libraries = models.ForeignKey(ta.models.lib.Library, on_delete = models.CASCADE)

    @property
    def username(self):
        return self.user.username

    @property
    def user_id(self):
        return self.user.user_id




class UserToken(models.Model):
    ...

class Route(models.Model):
    ...

