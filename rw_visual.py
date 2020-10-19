import matplotlib.pyplot as plt

from random_walk import RandomWalk

# generate multiple random walks while the program is active, colour the points, each walk 50000 points
while True:
    rw = RandomWalk(50000)
    rw.fill_walk()

    #set the size of the plotting window
    plt.figure(dpi = 128, figsize = (10,6))

    point_numbers = list(range(rw.num_points))

    # display the values on a scatter chart
    plt.scatter(rw.x_values, rw.y_values, c = point_numbers, cmap = plt.cm.Blues, edgecolor = 'none', s = 1)

    # you can also try
    # plt.plot(point_numbers, rw.x_values, rw.y_values, linewidth = 5)
    # to do this on a line graph

    # emphasise first and last points, plot each point with a size of 1
    plt.scatter(0, 0, c = 'green', edgecolors = 'none', s = 15)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c = 'red', edgecolors = 'none', s = 15)

    # remove the axes
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break