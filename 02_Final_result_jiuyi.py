import json
import string
import pandas as pd
import numpy as np
from attribute_func_jiuyi import *

def generate_df(attribute_list):
    df_list = []
    for attribute in attribute_list:
        if attribute == '@content@_ep@attribute@battery':
            df_battery = battery()
            df_list.append(df_battery)
        elif attribute == '@content@_ep@attribute@call':
            df_call = call()
            df_list.append(df_call)
        elif attribute == '@content@_ep@attribute@message':
            df_message = message()
            df_list.append(df_message)
        elif attribute == '@content@_ep@attribute@photo':
            df_photo = photo()
            df_list.append(df_photo)
        elif attribute == '@content@_ep@attribute@contacts':
            df_contacts = contacts()
            df_list.append(df_contacts)
        elif attribute == '@content@_ep@attribute@connect_wifi@ssid':
            df_conn_wifi = connected_wifi()
            df_list.append(df_conn_wifi)
        elif attribute == '@content@_ep@attribute@wifi_list':
            df_wifi_list = wifi_list()
            df_list.append(df_wifi_list)
        elif attribute == '@content@_ep@attribute@wifi_state':
            df_wifi_state = wifi_state()
            df_list.append(df_wifi_state)
    return df_list
def generate_result(df_list):
    final_df_2=pd.merge(df_list[0],df_list[1],on='@device_id')
    for index in range(2,len(df_list)):
        final_df_2 = pd.merge(final_df_2, df_list[index], on='@device_id')
    return final_df_2
if __name__=='__main__':
    attribute_list = ['@content@_ep@attribute@battery', '@content@_ep@attribute@call', '@content@_ep@attribute@message', '@content@_ep@attribute@photo', '@content@_ep@attribute@contacts',
                      '@content@_ep@attribute@connect_wifi@ssid', '@content@_ep@attribute@wifi_list', '@content@_ep@attribute@wifi_state']
    df_list=generate_df(attribute_list)
    final_df_2=generate_result(df_list)
    # print(final_df_2.head(10))

    final_df_2 = pd.merge(final_df_2, cc, on='@device_id')
    final_df_2.to_csv('merge_2.csv')
    print(final_df_2.head(10).transpose())
