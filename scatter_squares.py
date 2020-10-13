import matplotlib.pyplot as plt

# plots a dot at x = 2, y = 4 with style, left of x axis to right of x axis range = 0.2
plt.scatter(2, 4, s = 200)
plt.title("Square numbers", fontsize = 24)
plt.xlabel("Values", fontsize = 15)
plt.ylabel("Square of value", fontsize = 15)
plt.tick_params(axis = 'both', which = 'major', labelsize = 14)
plt.show()

# plot series of values, this time ask the machine to calculate the values
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, s = 40)
plt.axis([0, 1100, 0, 1100000])
plt.show()

# custom colour eg. red, remove outlines
plt.scatter(x_values, y_values, c='red', edgecolor='none', s=40)
plt.scatter(x_values, y_values, c=(0, 0, 0.8), edgecolor='none', s=40)

# colourmap
x_values = list(range(1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, c = y_values, cmap = plt.cm.Blues, edgecolor = 'none', s = 40)

# show and save file - use plt.savefig, trim whitespace using tight
plt.savefig('file_name.png', bbox_inches = 'tight')

