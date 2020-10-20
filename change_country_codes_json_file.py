import json
from country_codes import get_country_code
from pygal.maps.world import COUNTRIES

filename = 'population_data.json'
with open(filename) as f:
    data = json.load(f)
    for item in data:
        country = item['Country Name']
        code = get_country_code(country)
        if len(str(code)) > 2:
            item['Country Code'] = item['Country Code'].replace(str(code), str(COUNTRIES.keys()))
with open(filename) as r:
    json.dump(f, r, indent = 2)

print(data)
    
            

