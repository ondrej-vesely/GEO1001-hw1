#-- GEO1001.2020--hw01
#-- Ondrej Vesely
#-- 5162130

from collections import defaultdict

from _data import data
from _prompt import prompt


def bonus(data, treshold=25):
    try: treshold = int(treshold)
    except: treshold = 25

    temp_hours = defaultdict(int)

    for variables in data.values():
        dates = [dt.date() for dt in variables['FORMATTED DATE-TIME']['values']]
        temps = variables['Temperature']['values']
           
        for temp, date in zip(temps, dates):
            if temp > treshold:
                temp_hours[date] += temp

    ranking = sorted(temp_hours.items(), key=lambda x: x[0])


    print('''
If we turn on AC in temperatures over %s°C, 
3 most energy demanding days in time-series would be:
    ''' % treshold)
    for day, temp in reversed(ranking[-3:]):
        print(day.strftime('%A %d %B %Y'))

    print('\nThe 3 least demanding days would be:\n')
    for day, temp in ranking[:3]:
        print(day.strftime('%A %d %B %Y'))
           


# Main function to be called
def main():

    if prompt("Calculate most energy demending days?"):
        bonus(data, input('  AC activation treshold temp:  '))

if __name__ == '__main__':
    main()