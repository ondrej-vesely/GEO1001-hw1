#-- GEO1001.2020--hw01
#-- Ondrej Vesely
#-- 5162130

import numpy as np
import matplotlib.pyplot as plt

from _data import data
from _prompt import prompt


# Question 1
def print_stats(data):
    for variable, values in data['Sensor A'].items():
        if variable != 'FORMATTED DATE-TIME':
            name = ("%s [%s]:" % (variable, values['units']))
            print('\n', name, '_'*70, '\n')
        
            for sensor_name, sensor in data.items():
                print(sensor_name)
                v = sensor[variable]['values']
                print("    mean = %s  var = %s  st.var. = %s" % (v.mean(), v.var(), v.std()))


# Question 2
def show_histograms(data, bins=5):
    try: bins = int(bins)
    except: bins = 5
        
    variable = 'Temperature'
    fig = plt.figure(figsize=(28,4))

    for i, (sensor_name, sensor) in enumerate(data.items()):
        ax_index = int(100 + 10*len(data) + i + 1)
        ax = fig.add_subplot(ax_index)
        ax.hist(x=sensor[variable]['values'], 
                bins=bins, density=True, rwidth=0.85)
        ax.set_xlabel('%s [%s]' % (variable, sensor[variable]['units']))
        ax.set_ylabel('Frequency')
        ax.set_title(sensor_name)y

    plt.tight_layout(pad=3.0)
    plt.show()


# Question 3
def show_frequency(data, bins=20):
    try: bins = int(bins)
    except: bins = 20

    variable = 'Temperature'
    fig = plt.figure(figsize=(10,4))

    ax = fig.add_subplot(111)
    ax.set_title('Binned value frequency (%s bins)' % bins)

    for sensor_name, sensor in data.items():
        values = sensor[variable]['values']
        [frequency, bins] = np.histogram(values, 
                                        bins=bins)
        frequency = [f/len(values) for f in frequency]
        ax.plot(bins[:-1], frequency, 
                label=sensor_name)
        ax.set_xlabel('%s [%s]' % (variable, sensor[variable]['units']))
        ax.set_ylabel('Frequency')
        
    plt.legend(loc='upper right')
    plt.show()


# Question 4
def show_boxplots(data):
    fig = plt.figure(figsize=(13,4))

    subplots = [fig.add_subplot(131), 
                fig.add_subplot(132),
                fig.add_subplot(133)]

    variables = ['Wind Speed', 
                'Direction ‚ True', 
                'Temperature']

    for ax, variable in zip(subplots, variables):
        total_values = []
        for sensor_name, sensor in data.items():
            values = sensor[variable]['values']
            total_values.append(values)  
        ax.boxplot(total_values, showmeans=True, labels=data.keys())
        ax.set_ylabel('%s [%s]' % (variable, sensor[variable]['units']))
            
    plt.tight_layout()
    plt.show()



# Main function to be called
def main():

    if prompt("Print out mean statistics for all variables?"):
        print_stats(data)

    if prompt("Show histograms of Temperature measurments?"):
        show_histograms(data, input('  Number of bins:  '))

    if prompt("Show frequency plot for Temperature measurments?"):
        show_frequency(data, input('  Number of bins:  '))

    if prompt("Show boxplots for Wind Speed, Direction and Temperature?"):
        show_boxplots(data)


if __name__ == '__main__':
    main()