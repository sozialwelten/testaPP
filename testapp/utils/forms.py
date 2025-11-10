from geopy.geocoders import Nominatim
import re

import testapp as ta

geolocator = Nominatim(user_agent="TestaPP")

class address:
    def __init__(self, lat: float, long: float, **kwargs):
        """Tries to extract address data from geolocation by using Nominatim() from 
        geopy.

        lat: float
            Latitude. Rounds to 4 decimal places.
        long: float
            Longitude. Rounds to 4 decimal places.
        """
        self._long: float = round(long, 4)
        self._lat: float = round(lat, 4)
        self._addr: dict = address.getaddr(lat, long)

    @property
    def long(self) -> float:
        """Longitude. Rounded to 4 decimal places (ca. 7m)"""
        return self._long

    @property
    def lat(self) -> float:
        """Latitude. Rounded to 4 decimal places (ca. 7m)"""
        return self._lat
    @property
    def address(self) -> dict:
        """Address dictionary."""
        return self._addr

    @property
    def city(self) -> str|None:
        """City, or town, or village."""
        return self.address.get('city', 
                                self.address.get('town',
                                                 self.address.get('village', "")))
    @property
    def country(self) -> str|None:
        """Country"""
        return self._addr.get("country", "")

    @classmethod
    def getaddr(cls, lat: float, long: float) -> dict:
        """Get address as dictionary"""
        loc = geolocator.reverse((lat, long), language=ta.settings.LANGUAGE_CODE)   # type: ignore
        return loc.raw['address'] or {} # type: ignore

    def __format__(self, fmt_spec: str) -> str:
        """First formatting for address keys, then with traditional string formatting.
        Formats everything in @(...) with every [<key>].
        """
        match = re.match(rf"\s*\@\([^\)]\)\s*", fmt_spec)
        if not match:
            return str().__format__(fmt_spec)
        result = match.group()

        fmt_spec = fmt_spec[:match.start()] + fmt_spec[match.end():]

        for attr in ['city', 'country', 'long', 'lat']:
            result = result.replace(f"[{attr}]", getattr(self, attr, f"{attr.upper()}?"))
        return result.format(fmt_spec)
