from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    """Return 2 digit Pygal country code for the country, else return None"""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
        return None

