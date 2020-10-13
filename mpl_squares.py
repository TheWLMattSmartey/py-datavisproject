# Run code on terminal
# plt will be used as a reference to the graph plotting library
import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]
plt.plot(squares)

# plt.show() will display in graphical form in a new window
plt.show()

# modify line width, set title and axis labels, set size of tick labels
plt.plot(squares, linewidth = 5)
plt.title("Square numbers", fontsize = 24)
plt.xlabel("Values", fontsize = 15)
plt.ylabel("Square of value", fontsize = 15)
plt.tick_params(axis = 'both', labelsize = 14)
plt.plot(squares)
plt.show()

# introduce input values (x axis)
input_values = [1, 2, 3, 4, 5]

plt.title("Square numbers", fontsize = 24)
plt.xlabel("Values", fontsize = 15)
plt.ylabel("Square of value", fontsize = 15)
plt.tick_params(axis = 'both', labelsize = 14)

plt.plot(input_values, squares, linewidth = 5)
plt.show()





