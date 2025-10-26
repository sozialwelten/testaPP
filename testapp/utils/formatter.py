class NameFormat(str):
    __slots__ = ("parts",)
    _NAME_PARTS = [ "first", "middle", "last", "title", "suffix", "title" ]

    def __new__(cls, item) -> "NameFormat":
        inst = super().__new__(cls, str(item))
        inst.parts = [ inst ]
        return inst

    @classmethod
    def unlock(cls, other: str) -> "list[NameFormat]":
        var = other.replace("+", ";").replace("&", ";").replace("AND", ";")
        return [NameFormat(n.strip()) for n in other.split(";")]

    def __iter__(self):
        for p in (self.parts)
