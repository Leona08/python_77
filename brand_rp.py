import pandas as pd
import numpy as np
# data_df = pd.read_csv('aa')
# from read_json_xiaohang import *
import re

data2 = pd.read_csv(r'C:\Users\WFM\python\wool_data_analysis\data2_0524_3.csv')
i = 0
def brand_rp(attribute):
    if pd.isna(data2.loc[i, attribute]):
        value = np.NaN
    else:
        value = data2.loc[i, attribute]
    return value

def unibrand(br_list):
    if len(list(set(br_list))) == 1:
        s = 1
    else:
        s = 0
    return s

def build():
    # brand_list = list()
    if pd.isna(data2.loc[i, '@content@_ep@attribute@build_prop']):
        model = ''
        brand = ''
    else:
        build_ = data2.loc[i, '@content@_ep@attribute@build_prop']
        L = re.split('[|, =]', build_)
        if len(L) != 0:
            for index, value in enumerate(L):
                if 'ro.product.brand' in value and value == 'ro.product.brand':
                    brand_index = index
                    brand = str(L[index+1])
                if 'ro.product.model' in value and value == 'ro.product.model':
                    model_index = index
                    model = str(L[index+1])
                else:
                    brand = ''
                    model = ''
        else:
            brand = ''
            model = ''
    return brand, model
#
# for i in range(data2.shape[0]):
#     if model ==
dic_brand = dict()
dic_model = dict()
dic_rp = dict()
set_brand = dict()
set_model = dict()
set_rp = dict()
same_brand = list()
same_model = list()
prop_model = list()
prop_brand = list()

while i <= data2.shape[0]:
    if i == 0:
        br_list = []
        br_list.append(brand_rp('@content@_cp@brand'))
        # print(br_list)
        mo_list = []
        mo_list.append(brand_rp('@content@_cp@model'))
        rp_list = []
        rp_list.append(brand_rp('@content@_cp@rp'))

        brand, model = build()
        prop_brand.append(brand)
        prop_model.append(model)

        if brand != '' and pd.isna(data2.loc[i, '@content@_cp@brand']) == False and \
                brand == brand_rp('@content@_cp@brand'):
            same_brand.append(1)
        elif brand != '' and pd.isna(data2.loc[i, '@content@_cp@brand']) == False and \
                brand != brand_rp('@content@_cp@brand'):
            same_brand.append(0)
        else:
            same_brand.append(np.NaN)

        if model != '' and pd.isna(data2.loc[i, '@content@_cp@model']) == False and \
                model == brand_rp('@content@_cp@model'):
            same_model.append(1)
        elif model != '' and pd.isna(data2.loc[i, '@content@_cp@model']) == False and \
                model != brand_rp('@content@_cp@model'):
            same_model.append(0)
        else:
            same_model.append(np.NaN)



    elif i == data2.shape[0]:
        dic_brand.setdefault(data2.loc[i - 1, '@device_id'], list(set(br_list)))
        # dic_brand.setdefault(data_df.loc[i - 1, '@device_id'], set(br_list))
        dic_model.setdefault(data2.loc[i - 1, '@device_id'], list(set(mo_list)))
        # dic_brand.setdefault(data_df.loc[i - 1, '@device_id'], set(br_list))
        dic_rp.setdefault(data2.loc[i - 1, '@device_id'], list(set(rp_list)))
        # dic_brand.setdefault(data_df.loc[i - 1, '@device_id'], set(br_list))
        set_brand.setdefault(data2.loc[i - 1, '@device_id'], unibrand(br_list))
        set_model.setdefault(data2.loc[i - 1, '@device_id'], unibrand(mo_list))
        set_rp.setdefault(data2.loc[i - 1, '@device_id'], unibrand(rp_list))
    else:
        if data2.loc[i, '@device_id'] == data2.loc[i - 1, '@device_id']:
            br_list.append(brand_rp('@content@_cp@brand'))
            # mo_list = []
            mo_list.append(brand_rp('@content@_cp@model'))
            # rp_list = []
            rp_list.append(brand_rp('@content@_cp@rp'))

            brand, model = build()
            prop_brand.append(brand)
            prop_model.append(model)

            if brand != '' and pd.isna(data2.loc[i, '@content@_cp@brand']) == False and \
                    brand == brand_rp('@content@_cp@brand'):
                same_brand.append(1)
            elif brand != '' and pd.isna(data2.loc[i, '@content@_cp@brand']) == False and \
                    brand != brand_rp('@content@_cp@brand'):
                same_brand.append(0)
            else:
                same_brand.append(np.NaN)

            if model != '' and pd.isna(data2.loc[i, '@content@_cp@model']) == False and \
                    model == brand_rp('@content@_cp@model'):
                same_model.append(1)
            elif model != '' and pd.isna(data2.loc[i, '@content@_cp@model']) == False and \
                    model != brand_rp('@content@_cp@model'):
                same_model.append(0)
            else:
                same_model.append(np.NaN)

        else:
            dic_brand.setdefault(data2.loc[i - 1, '@device_id'], list(set(br_list)))
            dic_model.setdefault(data2.loc[i - 1, '@device_id'], list(set(mo_list)))
            dic_rp.setdefault(data2.loc[i - 1, '@device_id'], list(set(rp_list)))
            set_brand.setdefault(data2.loc[i - 1, '@device_id'], unibrand(br_list))
            set_model.setdefault(data2.loc[i - 1, '@device_id'], unibrand(mo_list))
            # print(set_model)
            set_rp.setdefault(data2.loc[i - 1, '@device_id'], unibrand(rp_list))
            br_list = []
            br_list.append(brand_rp('@content@_cp@brand'))
            mo_list = []
            mo_list.append(brand_rp('@content@_cp@model'))
            rp_list = []
            rp_list.append(brand_rp('@content@_cp@rp'))

            brand, model = build()
            prop_brand.append(brand)
            prop_model.append(model)

            if brand != '' and pd.isna(data2.loc[i, '@content@_cp@brand']) == False and \
                    brand == brand_rp('@content@_cp@brand'):
                same_brand.append(1)
            elif brand != '' and pd.isna(data2.loc[i, '@content@_cp@brand']) == False and \
                    brand != brand_rp('@content@_cp@brand'):
                same_brand.append(0)
            else:
                same_brand.append(np.NaN)

            if model != '' and pd.isna(data2.loc[i, '@content@_cp@model']) == False and \
                    model == brand_rp('@content@_cp@model'):
                same_model.append(1)
            elif model != '' and pd.isna(data2.loc[i, '@content@_cp@model']) == False and \
                    model != brand_rp('@content@_cp@model'):
                same_model.append(0)
            else:
                same_model.append(np.NaN)
    i = i+1

# print(dic_brand)
# print(dic_model)
att = [dic_brand, set_brand, dic_model, set_model, dic_rp, set_rp, prop_brand, prop_model, same_brand, same_model]
final_df = pd.DataFrame(att).transpose()
final_df = final_df.rename(columns={'index': '@device_id'})
# print(final_df)
final_df.to_csv('build_5_24_16_50.csv')