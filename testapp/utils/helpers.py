import os
import re
from typing import Pattern, Callable

def limit_text(limit: int,
               text: str,
               limited_hint: str|Callable[[str, int], str] = "...",
               ) -> str:
    """Takes a text and limits its length.

    limit: int
        Maximum displayed characters.
    text: str
        The text object.
    limit_hint: str | func(ORIG, LIMIT) -> str
        A hint, only displayed at the end of the string, when text was limited. Can be provided as a literal, or as a function, taking the original string and returning a string.
        Length will be substracted from limit.

    Returns:
        Limited string.
    """
    if len(text) < limit:
        return text
    if isinstance(limited_hint, Callable):
        hint: str = limited_hint(text, limit)
    else:
        hint = limited_hint
    return text[:limit - len(hint) - 1] + hint


def expand_url(base: str, *args: str) -> str:
    """Expands a URL without doubling '/'"""
    parts = []
    for part in [base, *args]:
        if part.endswith("/"):
            part = part[:-2]
        parts.append(part)
    return str("/").join(parts)

class HttpUrl(str):
    __slots__ = (
        "PROTOCOLL", "SUBDOMAIN", "TOP_LEVEL_DOMAIN",
        "PORT", "PATH", "QUERY", "FRAGMENT", "LOCAL",
    )
    _PTTRN: Pattern = re.compile(r"(https{0,1})://([^\.]+)\.([^/]+)(.*)")
    _LOCAL_PTTRN: Pattern = re.compile(r"(https{0,1})://(localhost):(\d+)(^[/]+)")

    def __new__(cls, item) -> "HttpUrl":
        item = str(item).replace("://www.", "://")
        
        inst = super().__new__(cls, item)

        if item.startswith("http"):
            item = "http://" + item

        if "localhost" in item.lower():
            inst.LOCAL = True
            match = cls._PTTRN.match(item)
        else:
            inst.LOCAL = False
            match = cls._LOCAL_PTTRN.match(item)

        if not match:
            raise SyntaxError()
        elif inst.LOCAL == True:
            inst.PROTOCOLL, domain, tail = match.groups()
            inst.TOP_LEVEL_DOMAIN = None
        else:
            inst.PROTOCOLL, domain, inst.TOP_LEVEL_DOMAIN, tail = match.groups()

        inst.SUBDOMAIN, port = domain.split(":", 1)
        if isinstance(port, str):
            inst.PORT = int(port)
        elif inst.LOCAL:
            inst.PORT = int(os.environ.get("PORT", 80))

        if not tail:
            inst.QUERY = inst.FRAGMENT = inst.PATH = None
            return inst
        tail, inst.FRAGMENT = tail.split("#", 1)
        inst.PATH, inst.QUERY = tail.split("?", 1)
        return inst

    def base_url(self, scheme: bool = True) -> str:
        result = ""
        if scheme:
            result += self.PROTOCOLL or ""
        if self.LOCAL:
            result += f"localhost:{self.PORT}"
        else:
            result += f"{self.SUBDOMAIN}.{self.TOP_LEVEL_DOMAIN}"

        return f"{result}.{self.TOP_LEVEL_DOMAIN}"

    def domain(self) -> str:
        return self.base_url(False)

    def __str__(self) -> str:
        result = f"{self.base_url(True)}{self.PATH}"
    
        for char, elem in zip(['?', '#'], [self.QUERY, self.PATH]):
            if elem:
                result = f"{result}{char}{elem}"
        return result

    def update(self, *path) -> None:
        self = HttpUrl(expand_url(str(self), *path))

    def __add__(self, other):
        if not isinstance(other, (str, HttpUrl)):
            raise TypeError("Invalid type")
        return HttpUrl(expand_url(str(self), other))

    def __iadd__(self, other) -> None:
        self.update(other)

    @classmethod
    def makelocal(
        cls,
        port: int|Callable[[str, int], int] = lambda env,default: int(os.environ.get(env, default)),
        _default_port: int = 80,
        _env_var: str = "PORT"   
    ) -> "HttpUrl":
        if isinstance(port, Callable):
            port = port(_env_var.upper(), _default_port)
        return HttpUrl(f"http://localhost:{port}")
