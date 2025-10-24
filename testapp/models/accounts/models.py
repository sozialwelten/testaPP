from django.db import models
from django.contrib.postgres.fields import ArrayField

from testapp.settings import DOMAIN
from testapp.utils.schemes import Token
from testapp.activitypub.actors import ActivityPubActor



class UserAccount(ActivityPubActor):
    name = models.CharField(max_length = 30)
    handle = models.CharField(max_length = 30)


class UserToken(models.Model):
    name = models.CharField(max_length = 10, unique = True)
    user = models.ForeignKey(UserAccount, on_delete = models.CASCADE, related_name = "tokens")

    @classmethod
    def auto_token(cls) -> Token:
        tkn = Token("a")
        if cls.objects.get(name = str(tkn)):
            tkn.next()
        return tkn

    @classmethod
    def get_free_tokens(cls, limit: int = 50) -> list[Token]:
        """Returns free tokens for current token length."""
        result: list[Token] = [cls.auto_token()]

        while len(result) <= limit:
            next_tkn = result[-1].next()
            if len(next_tkn) != len(result[-1]):
                break
            result.append(next_tkn)
        return result

    def __str__(self) -> Token:
        return Token(self.name)

class Route(models.Model):
    owner = models.CharField(max_length = 30)
    name = models.CharField(max_length = 30, unique = True)
    tag = models.CharField(max_length = 30, unique = True)

    id = models.CharField(max_length = 255)

    access_level = models.IntegerField(max_length = 1, default = AccessLevel.PRIVATE.value)

