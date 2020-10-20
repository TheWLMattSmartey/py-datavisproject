import json
import pygal.maps.world as worldmap
from country_codes import get_country_code

# load the world population data into a list
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

# build a dictionary of population data
cc_population = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country)
        if code:
            cc_population[code] = population

wm = worldmap.World()
wm.title = 'World populations in 2010 by country'
wm.add('2010', cc_population)

wm.render_to_file('world_population.svg')


