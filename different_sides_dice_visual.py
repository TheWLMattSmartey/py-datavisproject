from die import Die

import pygal

# create a D8 and a D12

die_1 = Die(8)
die_2 = Die(12)

# make 100000 rolls, store results in a list
results = [die_1.roll() + die_2.roll() for roll_num in range(100000)]

# analyse the results
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result + 1)]

# visualise the results
hist = pygal.Bar()

hist.title = "Results of rolling 1x D8 and 1x D12 dice 100000 times"
hist.x_labels = [str(x) for x in range(2, max_result+1)]
hist.x_title = "Result"
hist.y_title = "Frequency of result"

hist.add('D8 + D12', frequencies)
hist.render_to_file('different_sides_dice_visual.svg')
