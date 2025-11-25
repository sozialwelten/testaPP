from enum import Enum
# --- Models ---

# max_length for models.CharField()
CHAR_LEN_S = 12
CHAR_LEN_M = 60
CHAR_LEN_X = 120
CHAR_LEN_XL = 255

GEO_DEC_MAX = 4        # Decimal limit for ≈ 11m

# Page Group Names
class PageGroupNames(str, Enum):
    CACHES = "caches"
    ROUTES = "routes"
    LOGS = "logs"
    BOOKS = "books"
    ITEMS = "items"
    
DATETIME_ISO = "%Y-%m-%dT%H:%M:%S.%s%z"
