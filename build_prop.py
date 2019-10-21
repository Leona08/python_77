import numpy as np
import pandas as pd
import re
# data2 = pd.read_csv(r'C:\Users\WFM\python\wool_data_analysis\data2.csv')
data2 = pd.read_csv(r'C:\Users\WFM\python\wool_data_analysis\data2_0524_3.csv')



def build():
    # brand_list = list()
    if pd.isna(data2.loc[i, '@content@_ep@attribute@build_prop']):
        model = ''
        brand = ''
    else:
        build_ = data2.loc[i, '@content@_ep@attribute@build_prop']
        L = re.split('[|, =]', build_)
        # print(L)
        if len(L) != 0:
            for index, value in enumerate(L):
                if 'ro.product.brand' in L and value == 'ro.product.brand':
                    brand_index = index
                    brand = str(L[index+1])
                    # print(brand)
                if 'ro.product.model' in L and value == 'ro.product.model':
                    model_index = index
                    model = str(L[index+1])
                    # print(model)
                elif 'ro.product.brand' not in L:
                    brand = ''
                elif 'ro.product.model' not in L:
                    model = ''
        else:
            brand = ''
            model = ''
    return brand, model

data = data2.head(5000)
for i in range(data.shape[0]):
    brand, model = build()
    # print(L)
    if brand != '':
        print(brand)
    if model != '':
        print(model)