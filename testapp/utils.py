import pycountry
from babel import Locale

COUNTRY_CODES = [item.alpha_2 for item in pycountry.countries]

def get_country_name(code, output_lang: str = "EN") -> str:
    """Retrieves country name from country ISO code (de -> Germany)"""
    locale = Locale(output_lang)
    return locale.languages[code]
