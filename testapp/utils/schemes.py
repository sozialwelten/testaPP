import re
from string import ascii_uppercase

ORD_MOD = 65 # so that "A = 1" when using "ord()" 
ABC_LEN = 26

class Token(str):
    """For easier handling of user tokens.

    tkn = Token(1)          # "A"
    tkn = tkn + 1           # "B"
    tkn += 1                # "C"
    """
    def __new__(cls, item) -> "Token":
        if not item:
            raise SyntaxError("Item cannot be null or empty")
        elif isinstance(item, (int, float)) or str(item).isnumeric():
            return cls._from_int(int(item))
        elif not Token.check(item.upper()):
            raise SyntaxError(f"Invalid input. Use \"{ascii_uppercase}\".")
        return super().__new__(cls, str(item).upper())

    @classmethod
    def check(cls, other) -> bool:
        try:
            for char in list(str(other)):
                if not char in ascii_uppercase:
                    return False
            return True
        except:
            return False

    @classmethod
    def _from_int(cls, n) -> "Token":
        result = ""
        n = int(n)
        while n > 0:
            n, remainder = divmod(n - 1, 26)
            result = chr(65 + remainder) + result
        return Token(result)

    def __int__(self) -> int:
        n = 0
        for c in self:
            n = n * ABC_LEN + (ord(c.upper()) - (ORD_MOD - 1))
        return n

    def __iter__(self):
        for l in self.__str__():
            yield l

    def before(self, steps: int = 1) -> "Token":
        return Token(int(self) - steps)

    def next(self, steps: int = 1) -> "Token":
        return Token(int(self) + steps)

    def __add__(self, other) -> "Token":
        n = int(Token(other)) + int(self)
        return Token(n)

    def __rsub__(self, other) -> "Token":
        n = int(Token(other)) - int(self)
        return Token(n)

    def __sub__(self, other) -> "Token":
        n = int(self) - int(Token(other))
        return Token(n)
