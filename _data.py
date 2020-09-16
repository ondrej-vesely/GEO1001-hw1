#-- GEO1001.2020--hw01
#-- Ondrej Vesely
#-- 5162130

import pandas as pd
import numpy as np


def parse(path):
    """Parse heat stress sensor data excel sheets into dicts of value arrays."""
    
    raw_data = pd.read_excel(path)
    raw_data = np.array(raw_data)
    raw_data = np.swapaxes(raw_data, 0, 1)

    data = {}
    for column in raw_data:
        measure = column[2]
        units = column[3]
        values = column[4:]

        for i, val in enumerate(values):
            if isinstance(val, str):
                try:
                    values[i] = float(val)
                except:
                    pass

        data[measure] = {}
        data[measure]['unit'] = units
        data[measure]['vals'] = values
    
    return data


heat_a = parse('./data/HEAT - A_final.xls')
heat_b = parse('./data/HEAT - B_final.xls')
heat_c = parse('./data/HEAT - C_final.xls')
heat_d = parse('./data/HEAT - D_final.xls')
heat_e = parse('./data/HEAT - E_final.xls')
