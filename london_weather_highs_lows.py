import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'london_weather_09_2020.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    # print header name alongside its column, first column is value 0
    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # get temperature highs for each date
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_day = datetime.strptime(row[0], "%d/%m/%Y")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_day, "missing data")
        else:
            dates.append(current_day)
            highs.append(high)
            lows.append(low)

    # print("Temperature highs and lows for September: " + str(highs))

    # plot the data, alpha = transparency
    fig = plt.figure(dpi = 128, figsize = (10,6))
    plt.plot(dates, highs, c = 'red', alpha = 0.5)
    plt.plot(dates, lows, c = 'green', alpha = 0.5)
    plt.fill_between(dates, highs, lows, facecolor = 'blue', alpha = 0.1)

    # format plot
    plt.title("Daily high and low temperatures in London, September 2020", fontsize = 16)
    plt.xlabel('', fontsize = 16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize = 12)
    plt.tick_params(axis = 'both', which = 'major', labelsize = 12)

    plt.show()