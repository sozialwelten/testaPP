from enum import Enum
# --- Models ---

# max_length for models.CharField()
CHARFIELD_LEN_S = 12
CHARFIELD_LEN_M = 60
CHARFIELD_LEN_X = 120
CHARFIELD_LEN_XL = 255

MAX_GEO_DECIMALS = 4        # Decimal limit for ≈ 11m

# Page Group Names
class PageGroupNames(str, Enum):
    CACHES = "caches"
    ROUTES = "routes"
    LOGS = "logs"
    BOOKS = "books"
    ITEMS = "items"
    
DATETIME_ISO = "%Y-%m-%dT%H:%M:%S.%s%z"
