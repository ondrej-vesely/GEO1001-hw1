#-- GEO1001.2020--hw01
#-- Ondrej Vesely
#-- 5162130

import matplotlib.pyplot as plt	

from _data import *


def print_stats(data):
    for sensor_name, sensor in data.items():
        print('\n', sensor_name, '_'*70, '\n')
    
        for name, measure in sensor.items():
            if name != 'FORMATTED DATE-TIME':
                print("  %s [%s]:" % (name, measure['units']))
                v = measure['values']
                stats = (v.mean(), v.var(), v.std())
                print("    mean = %s  var = %s  st.var. = %s" % stats)


def show_histograms(data, bins=50):
    try:
        bins = int(bins)
    except:
        bins = 50
        
    variable = 'Temperature'
    fig = plt.figure(figsize=(28,4))

    for i, (sensor_name, sensor) in enumerate(data.items()):
        ax_index = int(100 + 10*len(data) + i + 1)
        ax = fig.add_subplot(ax_index)
        ax.hist(x=sensor[variable]['values'], 
                bins=bins, density=True, color='b', alpha=0.7, rwidth=0.85)
        ax.set_xlabel('%s [%s]' % (variable, sensor[variable]['units']))
        ax.set_ylabel('Frequency')
        ax.set_title(sensor_name)

    plt.tight_layout(pad=3.0)
    plt.show()


def main():
    if 'y' in input("Print out mean statistics for all variables? y/n:  "):
        print_stats(data)

    if 'y' in input("Show histograms of Temperature measurments? y/n:  "):
        show_histograms(data, input('Number of bins:  '))

main()