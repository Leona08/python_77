import pandas as pd
import numpy as np
# data_df = pd.read_csv('aa')
from math import radians, cos, sin, asin, fabs, sqrt
from read_json_xiaohang import *

def appKey():
    if pd.isna(data_df.loc[i, '@app_key']) == False:
        appkey = data_df.loc[i, '@app_key']
    else:
        appkey = 0
    return appkey
# app_key = [0, 'qqqq', '0', 'aaa', 0, 0]
def uniapp(app_key):
    if list(set(app_key)) == 1 and list(set(app_key))[0] == 0:
        app_value = np.NaN
    else:
        app_value = len([i for i in list(set(app_key)) if i!=0])
    return app_value

def netUni():
    if pd.isna(data_df.loc[i, '@content@_ep@net']) == False:
        net_value = (data_df.loc[i, '@content@_ep@net'])
    else:
        net_value = 0
    return net_value

# net_list = [a, 'wifi', 'aaa', 'sss', 'unknown']
def netValue(net_list):
    net_unique = list(data_df['@content@_ep@net'].unique())
    # net_unique = ['wifi', 'unknown', 'none', 'aaa', 'sss', 'bbb']
    dele = ['wifi', 'unknown', 'none']
    net_stay = list(set(net_unique) - set(dele))
    nozero = [i for i in list(net_list) if i!=0]
    net_uni = set(nozero) # net_list中的值唯一化,去空元素
    # print(net_uni)
    if len(list(set(net_list))) == 1 and list(set(net_list))[0] == 0:
        s = np.NaN
    else:
        if net_uni.issubset(net_stay) == True:
            s = 1
        elif net_uni.issubset(dele) == True:
            s = 0
        elif net_uni.issubset(dele) == False and net_uni.issubset(net_stay) == False:
            s = 1

    return s

def Carrier():
    if pd.isna(data_df.loc[i, '@content@_cp@carrier']) == False:
        carr_value = data_df.loc[i, '@content@_cp@carrier']
    else:
        carr_value = 0
    return carr_value
# carr_list = [0, 0, 0]
def carValue(carr_list):
    carrier_unique = list(data_df['@content@_cp@carrier'].unique())
    # carrier_unique = ['wifi', 'unknown', 'none', 'aaa', 'sss', 'bbb']
    dele = ['wifi', 'unknown', 'none']
    carrier_stay = list(set(carrier_unique) - set(dele))
    nozero = [i for i in list(carr_list) if i != 0]
    carr_uni = set(nozero)

    if len(list(set(carr_list))) == 1 and list(set(carr_list))[0] == 0:
        s = np.NaN
    else:
        if carr_uni.issubset(carrier_stay) == True:
            s = 1
        elif carr_uni.issubset(dele) == True:
            s = 0
        elif carr_uni.issubset(dele) == False and carr_uni.issubset(carrier_stay) == False:
            s = 1

    return s

def alarms():
    if pd.isna(data_df.loc[i, '@content@_ep@attribute@alarms']):
        alarm_value = 0
    elif data_df.loc[i, '@content@_ep@attribute@alarms'] == '':
        alarm_value = 1
    else:
        alarm_value = 2
    return alarm_value

def ala_value(alarm_list):
    if 2 in alarm_list:
        a = 1
    elif np.sum(alarm_list) == 0:
        a = np.NaN
    else:
        a = 0
    return a

def cmdline():
    if pd.isna(data_df.loc[i, '@content@_ep@attribute@cmdline']):
        cmdline_value = 0
    elif data_df.loc[i, '@content@_ep@attribute@cmdline'] == 'null':
        cmdline_value = 1
    else:
        cmdline_value = 2
    return cmdline_value

def cmd_value(cmd_list):
    if 2 in cmd_list:
        cmd = 1
    elif np.sum(cmd_list) == 0:
        cmd = np.NaN
    else:
        cmd = 0
    return cmd

def location():
    if pd.isna(data_df.loc[i, '@content@_ep@cell@location_area_code']):
        location_value = 0 # 空则为0，错则为1，对为2
    elif len(str(data_df.loc[i, '@content@_ep@cell@location_area_code'])) == 5:
        location_value = 2
    else:
        location_value = 1
    return location_value

def loc_value(loc_list):
    if 2 in loc_list:
        loc = 1
    elif np.sum(loc_list) == 0:
        loc = np.NaN
    else:
        loc = 0
    return loc

def pn(): # 1 全部为异常值
    if pd.isna(data_df.loc[i, '@content@_ep@attribute@pn']):
        pn_value = 0
    elif '|' in data_df.loc[i, '@content@_ep@attribute@pn']:
        pn_value = 1
    elif data_df.loc[i, '@content@_ep@attribute@pn'] == '+86' or data_df.loc[i, '@content@_ep@attribute@pn'] == '':
        pn_value = 1
    elif int(data_df.loc[i, '@content@_ep@attribute@pn']) == 0:
        pn_value = 1
    else:
        pn_value = 2
    return pn_value

def pn_value(pn_list):
    if 2 in pn_list:
        pnn = 1
    elif np.sum(pn_list) == 0:
        pnn = np.NaN
    else:
        pnn = 0

def imsi():
    if pd.isna(data_df.loc[i, '@content@_ep@attribute@imsi']):
        imsi_value = 0
    elif data_df.loc[i, '@content@_ep@attribute@imsi'] == '':
        imsi_value = 1
    elif '|' in data_df.loc[i, '@content@_ep@attribute@imsi']:
        imsi_value = 1
    else:
        imsi_value = 2
    return imsi_value

def imsi_value(imsi_list):
    if 2 in imsi_list:
        im = 1
    elif np.sum(imsi_list) == 0:
        im = np.NaN
    else:
        im = 0

def storage(): # count

    if pd.isna(data_df.loc[i, '@content@_ep@attribute@storage']):
        sto_value = np.NaN
        count = 0
    elif data_df.loc[i, '@content@_ep@attribute@storage'] == '':
        sto_value = np.NaN
        count = 0
    else:
        s = data_df.loc[i, '@content@_ep@attribute@storage'].split(' ')[1].split('/')
        sto_value = int(s[0])/int(s[1])
        count = 1
    return sto_value, count

# def sto_value(sto_list):

def adb():
    if pd.isna(data_df.loc[i, '@content@_ep@attribute@adb_status@adb']):
        adb_value = 0
    elif data_df.loc[i, '@content@_ep@attribute@adb_status@adb'] == True:
        adb_value = 2
    else:
        adb_value = 1
    return adb_value

def usb():
    if pd.isna(data_df.loc[i, '@content@_ep@attribute@adb_status@usbconnected']):
        usb_value = 0
    elif data_df.loc[i, '@content@_ep@attribute@adb_status@usbconnected'] == True:
        usb_value = 2
    else:
        usb_value = 1
    return usb_value

def adb_value(adb_list):
    if 2 in adb_list:
        adbb = 1
    elif np.sum(adb_list) == 0:
        adbb = np.NaN
    else:
        adbb = 0
    return adbb

def lbs():
    if pd.isna(data_df.loc[i, '@content@_ep@lbs']):
        value = 0
    elif data_df.loc[i, '@content@_ep@lbs'] == 'null':
        value = 0
    elif data_df.loc[i, '@content@_ep@lbs'] == '':
        value = 0
    else:
        value = str(data_df.loc[i, '@content@_ep@lbs'])
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
                # print(lat0)
                lat1 = radians(float(s[j][0]))
                # print(lat1)
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
            max, count = geodis(val)
    return max, count

# adb_list = [0, 0, 0]
# adbb= adb_value(adb_list)
# print(adbb)

def pedmet():
    if pd.isna(data_df.loc[i, '@content@_ep@attribute@pedometer@steps']) or \
            pd.isna(data_df.loc[i, '@content@_ep@attribute@pedometer@timestamp']):
        ped_value = np.NaN
        ped_time = np.NaN
        count = 0
    elif data_df.loc[i, '@content@_ep@attribute@pedometer@steps'] == 0 and \
            data_df.loc[i, '@content@_ep@attribute@pedometer@timestamp'] != 0:
        ped_value = 0
        ped_time = data_df.loc[i, '@content@_ep@attribute@pedometer@timestamp']
        count = 1
    elif data_df.loc[i, '@content@_ep@attribute@pedometer@steps'] == 0 and \
            data_df.loc[i, '@content@_ep@attribute@pedometer@timestamp'] == 0:
        ped_value = 0
        ped_time = 0
        count = 0
    elif data_df.loc[i, '@content@_ep@attribute@pedometer@steps'] != 0 and \
            data_df.loc[i, '@content@_ep@attribute@pedometer@timestamp'] != 0:

        ped_value = data_df.loc[i, '@content@_ep@attribute@pedometer@steps']
        ped_time = data_df.loc[i, '@content@_ep@attribute@pedometer@timestamp']
        count = 1

    return ped_value, ped_time, count

def error(L, method):
    s = [np.NaN]
    if list(set(L)) == s:
        value = np.NaN
    else:
        value = method(L)
    return value




dic_toal_count = dict()
dic_appkey = dict()
dic_net = dict()
dic_carr = dict()
dic_alarm = dict()
dic_cmd = dict()
dic_loc = dict()
dic_pn = dict()
dic_imsi = dict()
dic_sto_mean = dict()
dic_sto_var = dict()
dic_sto_count = dict()
dic_adb = dict()
dic_usb = dict()
dic_ped_mean = dict()
dic_ped_var = dict()
dic_ped_count = dict()
dic_ped_times = dict()
dic_lbs_max = dict()
dic_lbs_count = dict()

attr_list = [dic_toal_count, dic_appkey, dic_carr, dic_adb, dic_usb, dic_alarm, dic_cmd, dic_imsi, dic_ped_mean, dic_ped_var,
             dic_ped_count, dic_ped_times, dic_pn, dic_loc, dic_net, dic_sto_mean, dic_sto_var,
             dic_sto_count, dic_lbs_max, dic_lbs_count]
# len(attr_list)

count = 0

while i <= data_df.shape[0] :
    if i==0:
        app_key = []
        app_key.append(appKey())

        net_list = []
        net_list.append(netUni())

        carr_list = list()
        carr_list.append(Carrier())

        alarm_list = []
        alarm_list.append(alarms())

        cmd_list = list()
        cmd_list.append(cmdline())

        loc_list = list()
        loc_list.append(location())

        pn_list = list()
        pn_list.append(pn())

        imsi_list = list()
        imsi_list.append(imsi())

        sto_list = list()
        sto_value, storage_count = storage()
        sto_list.append(sto_value)
        sto_count = list()
        sto_count.append(storage_count)

        adb_list = list()
        adb_usb = list()
        adb_list.append(adb())
        adb_usb.append(usb())

        pedme_list = list()
        pedme_count = list()
        pedme_time = list()
        ped_value, ped_time, ped_count = pedmet()
        pedme_list.append(ped_value)
        pedme_count.append(ped_count)
        pedme_time.append(ped_time)

        lbs_list = []
        lbs_list.append(lbs())

        count=1
    elif i == data_df.shape[0]:
        dic_toal_count.setdefault(data_df.loc[i - 1, '@device_id'], count)
        dic_appkey.setdefault(data_df.loc[i - 1, '@device_id'], uniapp(app_key))
        dic_net.setdefault(data_df.loc[i - 1, '@device_id'], netValue(net_list))
        dic_carr.setdefault(data_df.loc[i - 1, '@device_id'], carValue(carr_list))
        dic_alarm.setdefault(data_df.loc[i - 1, '@device_id'], ala_value(alarm_list))
        dic_cmd.setdefault(data_df.loc[i - 1, '@device_id'], cmd_value(cmd_list))
        dic_loc.setdefault(data_df.loc[i - 1, '@device_id'], loc_value(loc_list))
        dic_pn.setdefault(data_df.loc[i - 1, '@device_id'], pn_value(pn_list))
        dic_imsi.setdefault(data_df.loc[i - 1, '@device_id'], imsi_value(imsi_list))
        dic_sto_mean.setdefault(data_df.loc[i - 1, '@device_id'], error(sto_list, np.nanmean))
        dic_sto_var.setdefault(data_df.loc[i - 1, '@device_id'], error(sto_list, np.nanvar))
        dic_sto_count.setdefault(data_df.loc[i - 1, '@device_id'], np.sum(sto_count))
        dic_adb.setdefault(data_df.loc[i - 1, '@device_id'], adb_value(adb_list))
        dic_usb.setdefault(data_df.loc[i - 1, '@device_id'], adb_value(adb_usb))
        dic_ped_mean.setdefault(data_df.loc[i - 1, '@device_id'], error(pedme_list, np.nanmean))
        dic_ped_var.setdefault(data_df.loc[i - 1, '@device_id'], error(pedme_list, np.nanvar))
        dic_ped_count.setdefault(data_df.loc[i - 1, '@device_id'], np.sum(pedme_count))
        dic_ped_times.setdefault(data_df.loc[i - 1, '@device_id'], error(pedme_time, np.nanmax))
        lbs_max, lbs_count = lbs_value()
        dic_lbs_max.setdefault(data_df.loc[i - 1, '@device_id'], lbs_max)
        dic_lbs_count.setdefault(data_df.loc[i - 1, '@device_id'], lbs_count)


    else:
        if data_df.loc[i, '@device_id'] == data_df.loc[i - 1, '@device_id']:
            app_key.append(appKey())

            net_list.append(netUni())

            carr_list.append(Carrier())

            alarm_list.append(alarms())

            cmd_list.append(cmdline())

            loc_list.append(location())

            pn_list.append(pn())

            sto_value, storage_count = storage()
            sto_list.append(sto_value)
            sto_count.append(storage_count)

            adb_list.append(adb())
            adb_usb.append(usb())

            ped_value, ped_time, ped_count = pedmet()
            pedme_list.append(ped_value)
            pedme_count.append(ped_count)
            pedme_time.append(ped_time)

            lbs_list.append(lbs())
            count = count + 1
        else:
            dic_toal_count.setdefault(data_df.loc[i - 1, '@device_id'], count)
            count = 1
            dic_appkey.setdefault(data_df.loc[i - 1, '@device_id'], uniapp(app_key))
            app_key = []
            app_key.append(appKey())

            dic_net.setdefault(data_df.loc[i - 1, '@device_id'], netValue(net_list))
            net_list = []
            net_list.append(netUni())

            dic_carr.setdefault(data_df.loc[i - 1, '@device_id'], carValue(carr_list))
            carr_list = []
            carr_list.append(Carrier())

            dic_alarm.setdefault(data_df.loc[i - 1, '@device_id'], ala_value(alarm_list))
            alarm_list = []
            alarm_list.append(alarms())

            dic_cmd.setdefault(data_df.loc[i - 1, '@device_id'], cmd_value(cmd_list))
            cmd_list = list()
            cmd_list.append(cmdline())

            dic_loc.setdefault(data_df.loc[i - 1, '@device_id'], loc_value(loc_list))
            loc_list = list()
            loc_list.append(location())

            dic_pn.setdefault(data_df.loc[i - 1, '@device_id'], pn_value(pn_list))
            pn_list = list()
            pn_list.append(pn())

            dic_sto_mean.setdefault(data_df.loc[i - 1, '@device_id'], error(sto_list, np.nanmean))
            dic_sto_var.setdefault(data_df.loc[i - 1, '@device_id'], error(sto_list, np.nanvar))
            dic_sto_count.setdefault(data_df.loc[i - 1, '@device_id'], np.sum(sto_count))
            sto_list = list()
            sto_value, storage_count = storage()
            sto_list.append(sto_value)
            sto_count = list()
            sto_count.append(storage_count)

            dic_adb.setdefault(data_df.loc[i - 1, '@device_id'], adb_value(adb_list))
            dic_usb.setdefault(data_df.loc[i - 1, '@device_id'], adb_value(adb_usb))
            adb_list = list()
            adb_usb = list()
            adb_list.append(adb())
            adb_usb.append(usb())

            dic_ped_mean.setdefault(data_df.loc[i - 1, '@device_id'], error(pedme_list, np.nanmean))
            dic_ped_var.setdefault(data_df.loc[i - 1, '@device_id'], error(pedme_list, np.nanvar))
            dic_ped_count.setdefault(data_df.loc[i - 1, '@device_id'], np.sum(pedme_count))
            dic_ped_times.setdefault(data_df.loc[i - 1, '@device_id'], error(pedme_time, np.nanmax))
            pedme_list = list()
            pedme_count = list()
            pedme_time = list()
            ped_value, ped_time, ped_count = pedmet()
            pedme_list.append(ped_value)
            pedme_count.append(ped_count)
            pedme_time.append(ped_time)

            lbs_max, lbs_count = lbs_value()
            dic_lbs_max.setdefault(data_df.loc[i - 1, '@device_id'], lbs_max)
            dic_lbs_count.setdefault(data_df.loc[i - 1, '@device_id'], lbs_count)

            lbs_list = []
            lbs_list.append(lbs())

    i = i + 1

# attr_list = [dic_toal_count, dic_appkey, dic_carr, dic_adb, dic_usb, dic_alarm, dic_cmd, dic_imsi, dic_ped_mean, dic_ped_var,
#              dic_ped_count, dic_ped_times, dic_pn, dic_loc, dic_net, dic_sto_mean, dic_sto_var,
#              dic_sto_count]
final_df = pd.DataFrame(attr_list).transpose().reset_index()
final_df = final_df.rename(columns={'index': '@device_id'})
print(final_df.head(5))
final_df.columns = ['@device_id', 'device_count', 'app_key', 'carrier', 'adb', 'usb',
                    'alarm', 'cmd', 'imsi', 'ped_mean', 'ped_var',
                    'ped_count', 'ped_times', 'pn', 'location', 'net',
                    'storage_mean', 'storage_var', 'storage_count', 'lbs_max', 'lbs_count']
print(final_df.head(5))
final_df.to_csv('attribute_tranf_0601_2159.csv')