#-- GEO1001.2020--hw01
#-- Ondrej Vesely
#-- 5162130

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd

from _data import data
from _prompt import prompt


# Question 1a
def show_cfd(data):
    variables = ['Temperature', 'Wind Speed']
    fig = plt.figure(figsize=(15,6))
    bins = 50

    for i, variable in enumerate(variables):
        for j, (sensor_name, sensor) in enumerate(data.items()):
            ax = plt.subplot2grid((len(variables),len(data)), (i,j))

            values = sensor[variable]['values']
            
            a = ax.hist(values, bins=bins, cumulative=True, alpha=0.0)
            ax.plot(a[1][1:]-(a[1][1:]-a[1][:-1])/2, a[0])
            ax.set_xlabel('%s [%s]' % (variable, sensor[variable]['units']))
            ax.set_ylabel('Cumulative distribution')
            
            if i == 0:
                ax.set_title(sensor_name)
        
    plt.tight_layout(pad=2.0)
    plt.show()


# Question 1b
def show_confidence(data):
    variables = ['Temperature', 'Wind Speed']
    confidence = lambda a: stats.t.interval(0.95, len(a)-1, 
                                            loc=np.mean(a), 
                                            scale=stats.sem(a))
    arr = []
    for i, variable in enumerate(variables):
        arr.append([])
        for sensor_name, sensor in data.items():
            values = sensor[variable]['values']
            arr[i].append('%.2f - %.2f' % confidence(values))

    df = pd.DataFrame(arr, columns=data.keys(), index=variables)
    print(df)

    if prompt("Save table as a CSV file?"):
        df.to_csv(input("Specify filename: "))
    




# Main function to be called
def main():

    if prompt("Show CFD plots for Temperature and Wind Speed?"):
        show_cfd(data)
    
    if prompt("Show 95% confidence interval for Temperature and Wind Speed?"):
        show_confidence(data)


if __name__ == '__main__':
    main()