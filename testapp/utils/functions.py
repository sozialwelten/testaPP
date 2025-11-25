from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from geopy import Point

import testapp as ta


_locator = Nominatim(user_agent="TestaPP")


def fetch_address(
    latitude: float,
    longitude: float,
    lang: str = ta.settings.LANGUAGE_CODE.lower()
) -> dict:
    """Takes geodata and returns address data. Lang has to be 2-letter language-code."""
    point: Point = Point((latitude, longitude))
    raw = _locator.reverse(point, language=lang).raw                                                    # type: ignore
    return raw.get('address', {})


def compare_location(
    x: Point|tuple[float, float],
    y: Point|tuple[float, float],
    tolerance: int = 6
) -> bool:
    """Takes to geo points, compares their distance and returns True, if identified 
    as identical, or False, if they are idenfified as different.

    x, y: geopy.Point | tuple<int, int>
        The geo points to be compared.
    tolerance: int
        Tolerance in meters, that is evaluated identical.
    """
    return geodesic(x, y).meters <= tolerance
