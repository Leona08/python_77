import json
import pandas as pd
import numpy as np
#df=pd.read_csv('df.csv',encoding = 'utf-8')
from read_json_xiaohang import *

def divUni(List):
    div = set()
    div_list = []
    for i in range(len(List)):
        app_key = []
        div_list.append(List[i]['@device_id'])
    div = set(div_list)
    div_uni = list(div)
    return div_uni

div_uni = divUni(data_list)
# print(div_uni)


# 找每一个device_id对应的app_key的unique数量
def appKey(List, div_uni):
    app_len = []
    for j in range(len(div_uni)):
        app = set()
        app_list = []
        for i in range(len(List)):
            if List[i]['@device_id'] == div_uni[j]:
                app_key = List[i]['@app_key']
                # print(app_key)
                app_list.append(app_key)
        # print(app_list)
        app = set(app_list)
        app_uni = list(app)
        # print(app_uni)
        # print(len(app_uni))
        app_len.append(len(app_uni))
    return app_len

app_len = appKey(data_list, div_uni)
# print(app_len)

# net处理
def netUni(List, div_uni, data):
    net_change = []
    net_unique = list(data['@content@_ep@net'].unique())
    dele = ['wifi', 'unknown', 'none']
    for i in range(len(dele)):
        if dele[i] in net_unique:
            net_unique.remove(dele[i])
    for j in range(len(div_uni)):
        net = set()
        net_list = []
        for i in range(len(List)):
            if List[i]['@device_id'] == div_uni[j]:
                net_1 = List[i]['@content@_ep@net']
                # print(net_1)
                net_list.append(net_1)
        net_uni = list(set(net_list))
        # print(net_uni)
        if set(net_uni).issubset(net_unique) == True:
            s = 1
            net_change.append(s)
        elif set(net_uni).issubset(dele) == False and set(net_uni).issubset(net_unique) == False:
            s = 1
            net_change.append(s)
        elif set(net_uni).issubset(dele) == True:
            s = 0
            net_change.append(s)
        elif len(net_uni) == 0:
            s = np.nan
            net_change.append(s)
    return net_change

net_change = netUni(data_list, div_uni, data2)
# print(net_change)

# carrier处理
def carrUni(List, div_uni, data):
    carrier_change = []
    carrier_unique = list(data['@content@_cp@carrier'].unique())
    dele = ['wifi', 'unknown', 'none']
    for i in range(len(dele)):
        if dele[i] in carrier_unique:
            carrier_unique.remove(dele[i])
    for j in range(len(div_uni)):
        carrier = set()
        carrier_list = []
        for i in range(len(List)):
            if List[i]['@device_id'] == div_uni[j]:
                carrier_1 = List[i]['@content@_cp@carrier']
                carrier_list.append(carrier_1)
        carrier_uni = list(set(carrier_list))
        # print(carrier_uni)
        if set(carrier_uni).issubset(carrier_unique) == True:
            s = 1
            carrier_change.append(s)
        elif set(carrier_uni).issubset(dele) == False and set(carrier_uni).issubset(carrier_unique) == False:
            s = 1
            carrier_change.append(s)
        elif set(carrier_uni).issubset(dele) == True:
            s = 0
            carrier_change.append(s)
        elif len(carrier_uni) == 0:
            s = np.nan
            carrier_change.append(s)
    return carrier_change
carrier_change = carrUni(data_list, div_uni, data2)
# print(carrier_change)

def alaUni(List, div_uni):
    alarm_change = []
    for j in range(len(div_uni)):
        # ala_set = set()
        alarm_list = []
        for i in range(len(List)):
            if List[i]['@device_id'] == div_uni[j]:
                if '@content@_ep@attribute@alarms' in List[i]:
                    alarm_1 = List[i]['@content@_ep@attribute@alarms']
                    alarm_list.append(alarm_1)
        alarm_uni = list(set(alarm_list))
        # print(alarm_uni)
        alarm_remo = [x for x in alarm_uni if x != ''] # ['']变成[]
        # print(alarm_remo)
        if len(alarm_remo) == 0:
            s = 0
            alarm_change.append(s)
        else:
            s = 1
            alarm_change.append(s)

    return alarm_change

alarm_change = alaUni(data_list, div_uni)
# print(alarm_change)

def cmdLine(List, div_uni):
    cmd_change = []
    for j in range(len(div_uni)):
        cmd_list = []
        for i in range(len(List)):
            if List[i]['@device_id'] == div_uni[j]:
                if '@content@_ep@attribute@cmdline' in List[i]:
                    cmd_list.append(List[i]['@content@_ep@attribute@cmdline'])
        cmd_uni = list(set(cmd_list))
        # print(cmd_uni)
        if len(cmd_uni) == 0 or cmd_uni[0] == 'null':
            s = 0
            cmd_change.append(s)
        else:
            s = 1
            cmd_change.append(s)
    return cmd_change
cmd_change = cmdLine(data_list, div_uni)

# location_area_code
def codeChange(List, div_uni):
    code_change = []
    for j in range(len(div_uni)):
        code_list = []
        for i in range(len(List)):
            if List[i]['@device_id'] == div_uni[j]:
                if '@content@_ep@cell@location_area_code' in List[i]:
                    code_list.append(List[i]['@content@_ep@cell@location_area_code'])
        # print(code_list)
        code_uni = list(set(code_list))
        # print(code_uni)
        if len(code_uni) == 0 or code_uni[0] == '0':
            s = 0
            code_change.append(s)
        else:
            s = 1
            code_change.append(s)
    return code_change
code_change = codeChange(data_list, div_uni)
# print(code_change)
# pn
def pnChange(List, div_uni):
    pn_change = []
    for j in range(len(div_uni)):
        pn_list = []
        for i in range(len(List)):
            if List[i]['@device_id'] == div_uni[j]:
                if '@content@_ep@attribute@pn' in List[i]:
                    pn_list.append(List[i]['@content@_ep@attribute@pn'])
        # print(code_list)
        pn_uni = list(set(pn_list))
        pn_remo = [x for x in pn_uni if x != '']
        # print(pn_remo)
        if len(pn_remo) == 0:
            s = 0
            pn_change.append(s)
        else:
            s = 1
            pn_change.append(s)
    return pn_change
pn_change = pnChange(data_list, div_uni)
# print(pn_change)

# imsi
def imSi(List, div_uni):
    imsi_change = []
    for j in range(len(div_uni)):
        imsi_list = []
        for i in range(len(List)):
            if List[i]['@device_id'] == div_uni[j]:
                if '@content@_ep@attribute@imsi' in List[i]:
                    imsi_list.append(List[i]['@content@_ep@attribute@imsi'])
        # print(imsi_list)
        imsi_uni = list(set(imsi_list))
        # print(imsi_uni)
        imsi_remo = [x for x in imsi_uni if x != '']
        if len(imsi_remo) != 0 and '|' in imsi_remo[0]:
            s = 2
            imsi_change.append(s)
        elif len(imsi_remo) == 0:
            s = 0
            imsi_change.append(s)
        else:
            s = 1
            imsi_change.append(s)
    return imsi_change
imsi_change = imSi(data_list, div_uni)
# print(imsi_change)

def storChange(List, div_uni):
    storage_mean = []
    storage_vari = []
    for j in range(len(div_uni)):
        sto_list = []
        for i in range(len(List)):

            if List[i]['@device_id'] == div_uni[j]:
                if '@content@_ep@attribute@storage' in List[i]:
                    S = List[i]['@content@_ep@attribute@storage'].split(' ')[1].split('/')
                    sto_list.append(int(S[0])/int(S[1]))
        storage_mean.append(np.mean(sto_list))
        storage_vari.append(np.var(sto_list))
    return storage_mean,storage_vari

storage_mean, storage_vari = storChange(data_list, div_uni)

# print(storage_mean)
# print(storage_vari)



# adb_status
import json
def aDb(List, div_uni):
    adb_adb = []
    adb_usb = []
    for j in range(len(div_uni)):
        adb_list = []
        usb_list = []
        for i in range(len(List)):
            if List[i]['@device_id'] == div_uni[j]:
                if '@content@_ep@attribute@adb_status@adb' in List[i]:
                    adb_list.append(List[i]['@content@_ep@attribute@adb_status@adb'])
                if '@content@_ep@attribute@adb_status@usbconnected' in List[i]:
                    usb_list.append(List[i]['@content@_ep@attribute@adb_status@usbconnected'])

        adb_uni = list(set(adb_list))
        usb_uni = list(set(usb_list))
        # print('adb: ', adb_uni, len(adb_uni))
        # print('usb:', usb_list)
        if len(adb_uni) != 0:
            if adb_uni[0] == False:
                m = 0
                adb_adb.append(m)
            elif adb_uni[0] == True:
                m = 1
                adb_adb.append(m)
        else:
            m = np.nan
            adb_adb.append(m)

        if len(usb_uni) != 0:
            if usb_uni[0] == False:
                m = 0
                adb_usb.append(m)
            elif usb_uni[0] == True:
                m = 1
                adb_usb.append(m)
        else:
            m = np.nan
            adb_usb.append(m)
    return adb_adb, adb_usb
adb_adb, adb_usb = aDb(data_list, div_uni)
# print(adb_usb)
# print(adb_adb)

# pedmoter  这个还没有做完 关键是 没有找到一个device对应多个的
def pedMoter(List, div_uni):
    ped_mean = []
    ped_varia = list()
    ped_time = []
    for j in range(len(div_uni)):
        ped_list = []
        time_list = []
        for i in range(len(List)):
            if List[i]['@device_id'] == div_uni[j]:
                if '@content@_ep@attribute@pedometer@steps' in List[i] and List[i]['@content@_ep@attribute@pedometer@timestamp'] != '0':
                    ped_list.append(List[i]['@content@_ep@attribute@pedometer@steps'])  # 如果一个device_id有多个值，则会附加吧
                    time_list.append(List[i]['@content@_ep@attribute@pedometer@timestamp'])
        # print(ped_list)
        # print('------')
        # print(time_list)
        count = []
        for m in range(len(ped_list)):
            if ped_list[m] != 0 and len(ped_list) != 0:
                count.append(m)
        maxtime = 0
        for i in range(len(count)):
            if time_list[count[i]] > maxtime:
                maxtime = time_list[count[i]]
        ped_time.append(maxtime)
        ped_mean.append(np.mean(ped_list))
        ped_varia.append(np.var(ped_list))

    return ped_mean, ped_varia, ped_time


ped_mean, ped_varia, ped_time = pedMoter(data_list, div_uni)

from pandas.core.frame import DataFrame
c = {"@device_id" : div_uni, 'app_key':app_len, 'net':net_change, 'carrier':carrier_change,
     "ped_mean": ped_mean, 'ped_vari':ped_varia,  'ped_time':ped_time, 'abd':adb_adb, 'abd_usb':adb_usb,
     'imsi': imsi_change, 'alarms':alarm_change, 'pn':pn_change,
     'cmdline': cmd_change, 'location_area_code': code_change, 'storage_mean': storage_mean,
     'storage_vari':storage_vari}#将列表a，b转换成字典
cc = DataFrame(c)
cc.to_csv('attribute_fengmin.csv')