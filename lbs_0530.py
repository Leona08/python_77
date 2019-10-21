from math import radians, cos, sin, asin, fabs, sqrt
import numpy as np
import pandas as pd
def lbs():
    if pd.isna(data_df.loc[i, '@content@_ep@lbs']):
        value = 0
    elif data_df.loc[i, '@content@_ep@lbs'] == 'null':
        value = 0
    elif data_df.loc[i, '@content@_ep@lbs'] == '':
        value = 0
    else:
        value = data_df.loc[i, '@content@_ep@lbs']
    return value

def geodis(l):
    s = []
    lis = []
    for m in range(len(l)):
        s.append(l[m].split(','))
    for i in range(len(s)):
        for j in range(len(s)):
            if i < j:
                lat0 = radians(float(s[i][0]))
                print(lat0)
                lat1 = radians(float(s[j][0]))
                print(lat1)
                lng0 = radians(float(s[i][1]))
                lng1 = radians(float(s[j][1]))
                r = 6371

                dlng = fabs(lng0 - lng1)
                dlat = fabs(lat0 - lat1)
                h = sin(dlat/2)**2 + cos(lat0) * cos(lat1) * sin(dlng/2) ** 2
                distance = 2 * r * asin(sqrt(h))
                lis.append(distance)
                # min = np.min(lis)
                max = np.max(lis)
                count = len(lis)
    return max, count


def lbs_value():
    l = list(set(lbs_list))
    if len(l) == 1 and l[0] == 0:
        # min = np.NaN
        max = np.NaN
        count = np.NaN
    elif len(l) == 1 and l[0] != 0:
        # min = np.NaN
        max = np.NaN
        count = 1
    elif len(l) != 1:
        val = [i for i in l if i != 0]
        if len(val) == 1:
            # min = np.NaN
            max = np.NaN
            count = 1
        else:
            max, count = geodis(l)
    return max, count


# l = ['31.62871,120.13085', '26.604523,101.634412', '22.607643062342177,108.18147281958535']
# l = ['110.0123, 23.32435', '129.1344,25.5465']
# l = ['22.599578, 113.973129', '34.0522342, -118.2436849']

    # m.extend(l[i].split(','))


