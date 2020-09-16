#-- GEO1001.2020--hw01
#-- Ondrej Vesely
#-- 5162130


from _data import *


def print_stats(data):
    for sensor_name, sensor in data.items():
        print('\n', sensor_name, '_'*70, '\n')
    
        for name, measure in sensor.items():
            if name != 'FORMATTED DATE-TIME':
                print("  %s [%s]:" % (name, measure['units']))
                v = measure['values']
                print("    mean = %s  var = %s  st.var. = %s" % (v.mean(), v.var(), v.std()))


def main():
    if 'y' in input("Print out mean statistics for all variables? y/n:  "):
        print_stats(data)

main()