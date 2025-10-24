from django.db import models
from django.contrib.postgres.fields import ArrayField

from testapp.settings import DOMAIN
from testapp.utils.schemes import Token, AccessLevel
from items.models import Book

class Route(models.Model):
    owner = models.CharField(max_length = 30)
    name = models.CharField(max_length = 30, unique = True)
    tag = models.CharField(max_length = 30, unique = True)

    access_level = models.IntegerField(max_length = 1, default = AccessLevel.PRIVATE.value)
    maintainer = ArrayField(models.CharField(max_length = 30))

    def __str__(self):
        return f"{ self.name }@{ DOMAIN }"

    def __repr__(self):
        return f"[route@{ DOMAIN }]"


class UserAccount(models.Model):
    handle = models.CharField(max_length = 30, blank = False, null = False)
    name = models.CharField(max_length = 30, blank = False, null = False)

    def __str__(self):
        return f"{ self.name }@{ self.handle }@{ DOMAIN }"

    def __repr__(self):
        return f"USER[@{ DOMAIN }]:{ self.handle }"


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

    def __repr__(self) -> str:
        return f"TOKEN[@{ self.user.name }@{ DOMAIN }]:{ self.name }"
