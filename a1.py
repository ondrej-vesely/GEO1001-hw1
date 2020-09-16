#-- GEO1001.2020--hw01
#-- Ondrej Vesely
#-- 5162130

import numpy as np
import matplotlib.pyplot as plt

from _data import data


# Question 1
def print_stats(data):
    for sensor_name, sensor in data.items():
        print('\n', sensor_name, '_'*70, '\n')
    
        for name, measure in sensor.items():
            if name != 'FORMATTED DATE-TIME':
                print("  %s [%s]:" % (name, measure['units']))
                v = measure['values']
                stats = (v.mean(), v.var(), v.std())
                print("    mean = %s  var = %s  st.var. = %s" % stats)


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
                bins=bins, density=True, color='b', alpha=0.7, rwidth=0.85)
        ax.set_xlabel('%s [%s]' % (variable, sensor[variable]['units']))
        ax.set_ylabel('Frequency')
        ax.set_title(sensor_name)

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

    def promt(question):
        print('\n')
        while True:
            reply = str(input(question+' (y/n): ')).lower().strip()
            if reply[:1] == 'y':
                return True
            if reply[:1] == 'n':
                return False

    if promt("Print out mean statistics for all variables?"):
        print_stats(data)

    if promt("Show histograms of Temperature measurments?"):
        show_histograms(data, input('  Number of bins:  '))

    if promt("Show frequency plot for Temperature measurments?"):
        show_frequency(data, input('  Number of bins:  '))

    if promt("Show frequency plot for Temperature measurments?"):
        show_boxplots(data)


if __name__ == '__main__':
    main()