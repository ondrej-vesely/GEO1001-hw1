#-- GEO1001.2020--hw01
#-- Ondrej Vesely
#-- 5162130

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from _data import data


# Question1
def show_distr(data, bins=50):
    try: bins = int(bins)
    except: bins = 50

    variable = 'Temperature'
    fig = plt.figure(figsize=(18,10))

    # PMF
    for i, (sensor_name, sensor) in enumerate(data.items()):
        ax = plt.subplot2grid((3,5), (0,i))
        values = pd.Series(sensor[variable]['values'])
        values = values.value_counts() / len(values)
        
        a = ax.bar(values.index, values)
        ax.set_ylim(0, 0.025)
        ax.set_xlabel('%s [%s]' % (variable, sensor[variable]['units']))
        ax.set_ylabel('Probability Mass (%s values)' % len(values))
        ax.set_title(sensor_name)

    # PDF
    for i, (sensor_name, sensor) in enumerate(data.items()):
        ax = plt.subplot2grid((3,5), (1,i))
        values = sensor[variable]['values']
        
        a = ax.hist(values, bins=bins, density=True, alpha=0.5)
        hist_x, hist_y = (a[1][1:]-(a[1][1:]-a[1][:-1])/2, a[0])
        ax.plot(hist_x, hist_y)
        ax.set_ylim(0, 0.2)
        ax.set_xlabel('%s [%s]' % (variable, sensor[variable]['units']))
        ax.set_ylabel('Probability Density (%s bins)' % bins)

    # CDF
    for i, (sensor_name, sensor) in enumerate(data.items()):
        ax = plt.subplot2grid((3,5), (2,i))
        values = sensor[variable]['values']
        
        a = ax.hist(values, bins=bins, cumulative=True, alpha=0.0)
        ax.plot(a[1][1:]-(a[1][1:]-a[1][:-1])/2, a[0])
        ax.set_xlabel('%s [%s]' % (variable, sensor[variable]['units']))
        ax.set_ylabel('Cumulative distribution')
    
    plt.tight_layout(pad=2.0)
    plt.show()


# Question 2
def show_kernel(data):
    pass



# Main function to be called
def main():

    def promt(question):
        print('\n')
        while True:
            reply = str(input(question+' (y/n): ')).lower().strip()
            if reply[:1] == 'y':
                return True
            if reply[:1] == 'n':
                return False

    if promt("Show PMF, PDF and CDF distribution plots?"):
        show_distr(data, input('  Number of PDF bins:  '))


if __name__ == '__main__':
    main()