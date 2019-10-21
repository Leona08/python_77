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

device_list=list(set(data2['@device_id']))
L=len(device_list)

def battery():
    new_df = data2.set_index(['@device_id', '@content@_ep@timestamp'])
    df_battery=new_df.loc[:,['@content@_ep@attribute@battery']]
    update_df = pd.DataFrame()
    data_mean = []
    data_var = []
    for index in range(L):
        df_device = df_battery.loc[[device_list[index]], :]
        l = len(df_device)
        for i in range(l):
            value = df_device.iloc[i, :].values  # value:array
            if np.any(pd.isna(value) != True):
                for j in range(len(list(value))):
                    if (list(value))[j] != '':
                        v = int((list(value))[j].split('/')[0])
                        if v != -1:
                            df_device.iloc[i, 0] = v
                        else:
                            df_device.iloc[i, 0] = np.NaN
            else:
                df_device.iloc[i, 0] = np.NaN
        update_df = update_df.append(df_device)
    for index in range(L):
        dv_list = []
        df_update_device = update_df.loc[[device_list[index]], :]
        mean = float(df_update_device.mean())
        dv_list.append(device_list[index])
        dv_list.append(mean)
        data_mean.append(dv_list)
    arry_mean = np.array(data_mean)
    df_mean = pd.DataFrame(arry_mean, columns=['@device_id', 'battery_mean'])
    for index in range(L):
        dv_list = []
        df_update_device = update_df.loc[[device_list[index]], :]
        var = float(df_update_device.var())
        dv_list.append(device_list[index])
        dv_list.append(var)
        data_var.append(dv_list)
    arry_var = np.array(data_var)
    df_var = pd.DataFrame(arry_var, columns=['@device_id', 'battery_var'])
    final_df = pd.merge(df_mean, df_var, on='@device_id')
    return final_df

# final_df = battery()
# print(final_df)
# print(final_df.head(5))

def call():
    update_df = pd.DataFrame()
    new_df = data2
    df_call = new_df.loc[:, ['@device_id', '@content@_ep@timestamp', '@content@_ep@attribute@call']]
    call_num = []
    call_dur = []
    call_diff = []
    for index in range(L):
        df_device = df_call.loc[df_call['@device_id'] == device_list[index]]
        df_device = df_device.loc[df_device['@content@_ep@timestamp'] == df_device['@content@_ep@timestamp'].max()]
        update_df = update_df.append(df_device)
    for index in range(L):
        upd_df = update_df.loc[update_df['@device_id'] == device_list[index]]
        value = upd_df['@content@_ep@attribute@call'].values
        dv_list = []
        counts = 0
        if np.any(pd.isna(value) != True):
            for j in range(len(list(value))):
                if (list(value))[j] != '':
                    value_list = json.loads((list(value))[j])
                    length = len(value_list)
                    if length != 0:
                        counts = counts + length

                    else:
                        counts = counts
            dv_list.append(device_list[index])
            dv_list.append(counts)


        else:
            dv_list.append(device_list[index])
            dv_list.append(np.NaN)
        call_num.append(dv_list)
    arry_num = np.array(call_num)
    df_num = pd.DataFrame(arry_num, columns=['@device_id', 'call_num'])
    for index in range(L):
        upd_df = update_df.loc[update_df['@device_id'] == device_list[index]]
        value = upd_df['@content@_ep@attribute@call'].values
        dv_list = []
        date_max = 0
        if np.any(pd.isna(value) != True):
            for k in range(len(list(value))):
                if (list(value))[k] != '':
                    value_list = json.loads((list(value))[k])
                    if len(value_list) != 0:
                        for j in range(len(value_list)):
                            dic = value_list[j]
                            c_date = dic.get('date', '0')
                            if c_date.isdigit() == True:
                                call_date = int(c_date)
                                if call_date > date_max:
                                    date_max = call_date
                            else:
                                date_max = np.NaN
                    else:
                        date_max = np.NaN
        else:
            date_max = np.NaN
        dv_list.append(device_list[index])
        date_diff = int((upd_df['@content@_ep@timestamp'].values)[0]) - date_max
        dv_list.append(date_diff)
        call_diff.append(dv_list)
    arry_diff = np.array(call_diff)
    df_diff = pd.DataFrame(arry_diff, columns=['@device_id', 'call_diff'])
    for index in range(L):
        upd_df = update_df.loc[update_df['@device_id'] == device_list[index]]
        value = upd_df['@content@_ep@attribute@call'].values
        dv_list = []
        duration = 0
        if np.any(pd.isna(value) != True):
            for k in range(len(list(value))):
                if (list(value))[k] != '':
                    value_list = json.loads((list(value))[k])
                    if len(value_list) != 0:
                        for j in range(len(value_list)):
                            dic = value_list[j]
                            c_dur = dic.get('duration', '0')
                            if c_dur.isdigit() == True:
                                dur = int(c_dur)
                                duration = duration + dur
                            else:
                                duration = np.NaN
                    else:
                        duration = np.NaN
        else:
            duration = np.NaN
        dv_list.append(device_list[index])
        dv_list.append(duration)
        call_dur.append(dv_list)
    arry_dur = np.array(call_dur)
    df_dur = pd.DataFrame(arry_dur, columns=['@device_id', 'call_duration'])
    final_df = pd.merge(df_num, df_dur, on='@device_id')
    Final_df = pd.merge(final_df, df_diff, on='@device_id')
    return Final_df
# Final_df = call()
# print(Final_df)

def message():
    update_df = pd.DataFrame()
    new_df = data2
    df_msg = new_df.loc[:, ['@device_id', '@content@_ep@timestamp', '@content@_ep@attribute@message']]
    msg_num = []
    msg_diff = []
    for index in range(L):
        df_device = df_msg.loc[df_msg['@device_id'] == device_list[index]]
        df_device = df_device.loc[df_device['@content@_ep@timestamp'] == df_device['@content@_ep@timestamp'].max()]
        update_df = update_df.append(df_device)
    for index in range(L):
        upd_df = update_df.loc[update_df['@device_id'] == device_list[index]]
        value = upd_df['@content@_ep@attribute@message'].values
        dv_list = []
        counts = 0
        if np.any(pd.isna(value) != True):
            for j in range(len(list(value))):
                if (list(value))[j] != '':
                    value_list = json.loads((list(value))[j])
                    length = len(value_list)
                    if length != 0:
                        counts = counts + length

                    else:
                        counts = counts
            dv_list.append(device_list[index])
            dv_list.append(counts)
        else:
            dv_list.append(device_list[index])
            dv_list.append(np.NaN)
        msg_num.append(dv_list)
    arry_num = np.array(msg_num)
    df_num = pd.DataFrame(arry_num, columns=['@device_id', 'message_num'])
    for index in range(L):
        upd_df = update_df.loc[update_df['@device_id'] == device_list[index]]
        value = upd_df['@content@_ep@attribute@message'].values
        dv_list = []
        date_max = 0
        if np.any(pd.isna(value) != True):
            for k in range(len(list(value))):
                if (list(value))[k] != '':
                    value_list = json.loads((list(value))[k])
                    if len(value_list) != 0:
                        for j in range(len(value_list)):
                            dic = value_list[j]
                            m_date = dic.get('date', '0')
                            if m_date.isdigit() == True:
                                msg_date = int(m_date)
                                if msg_date > date_max:
                                    date_max = msg_date
                            else:
                                date_max = np.NaN

                    else:
                        date_max = np.NaN
        else:
            date_max = np.NaN
        dv_list.append(device_list[index])
        date_diff = int((upd_df['@content@_ep@timestamp'].values)[0]) - date_max
        dv_list.append(date_diff)
        msg_diff.append(dv_list)
    arry_diff = np.array(msg_diff)
    df_diff = pd.DataFrame(arry_diff, columns=['@device_id', 'message_diff'])
    final_df = pd.merge(df_num, df_diff, on='@device_id')
    return final_df
# final_df = message()
# print(final_df)

def photo():
    update_df = pd.DataFrame()
    new_df = data2
    df_photo = new_df.loc[:, ['@device_id', '@content@_ep@timestamp', '@content@_ep@attribute@photo']]
    photo_num = []
    photo_diff = []
    for index in range(L):
        df_device = df_photo.loc[df_photo['@device_id'] == device_list[index]]
        df_device = df_device.loc[df_device['@content@_ep@timestamp'] == df_device['@content@_ep@timestamp'].max()]
        update_df = update_df.append(df_device)

    for index in range(L):
        upd_df = update_df.loc[update_df['@device_id'] == device_list[index]]
        value = upd_df['@content@_ep@attribute@photo'].values
        dv_list = []
        counts = 0
        if np.any(pd.isna(value) != True):
            for j in range(len(list(value))):
                if (list(value))[j] != '':
                    value_list = json.loads((list(value))[j])
                    length = len(value_list)
                    if length != 0:
                        counts = counts + length

                    else:
                        counts = counts
            dv_list.append(device_list[index])
            dv_list.append(counts)
        else:
            dv_list.append(device_list[index])
            dv_list.append(np.NaN)
        photo_num.append(dv_list)
    arry_num = np.array(photo_num)
    df_num = pd.DataFrame(arry_num, columns=['@device_id', 'photo_num'])

    for index in range(L):
        upd_df = update_df.loc[update_df['@device_id'] == device_list[index]]
        value = upd_df['@content@_ep@attribute@photo'].values
        dv_list = []
        date_max = 0
        if np.any(pd.isna(value) != True):
            for k in range(len(list(value))):
                if (list(value))[k] != '':
                    value_list = json.loads((list(value))[k])
                    if len(value_list) != 0:
                        for j in range(len(value_list)):
                            dic = value_list[j]
                            p_date = dic.get('datetaken', '0')
                            if p_date.isdigit() == True:
                                photo_date = int(p_date)
                                if photo_date > date_max:
                                    date_max = photo_date
                            else:
                                date_max = np.NaN
                    else:
                        date_max = np.NaN
        else:
            date_max = np.NaN
        dv_list.append(device_list[index])
        date_time = int((upd_df['@content@_ep@timestamp'].values)[0])
        date_diff = date_time - date_max
        dv_list.append(date_diff)
        photo_diff.append(dv_list)
    arry_diff = np.array(photo_diff)
    df_diff = pd.DataFrame(arry_diff, columns=['@device_id', 'photo_diff'])
    final_df = pd.merge(df_num, df_diff, on='@device_id')
    return final_df
# final_df = photo()
# print(final_df)

def contacts():
    update_df = pd.DataFrame()
    new_df = data2
    df_contact = new_df.loc[:, ['@device_id', '@content@_ep@timestamp', '@content@_ep@attribute@contacts']]
    contact_num = []
    contact_diff = []
    contact_count = []  # 累计联系次数
    for index in range(L):
        df_device = df_contact.loc[df_contact['@device_id'] == device_list[index]]
        df_device = df_device.loc[df_device['@content@_ep@timestamp'] == df_device['@content@_ep@timestamp'].max()]
        update_df = update_df.append(df_device)
    for index in range(L):
        upd_df = update_df.loc[update_df['@device_id'] == device_list[index]]
        value = upd_df['@content@_ep@attribute@contacts'].values
        dv_list = []
        counts = 0
        if np.any(pd.isna(value) != True):
            for j in range(len(list(value))):
                if (list(value))[j] != '':
                    value_list = json.loads((list(value))[j])
                    length = len(value_list)
                    if length != 0:
                        counts = counts + length

                    else:
                        counts = counts
            dv_list.append(device_list[index])
            dv_list.append(counts)
        else:
            dv_list.append(device_list[index])
            dv_list.append(np.NaN)
        contact_num.append(dv_list)
    arry_num = np.array(contact_num)
    df_num = pd.DataFrame(arry_num, columns=['@device_id', 'contacts_num'])
    for index in range(L):
        upd_df = update_df.loc[update_df['@device_id'] == device_list[index]]
        value = upd_df['@content@_ep@attribute@contacts'].values
        dv_list = []
        date_max = 0
        if np.any(pd.isna(value) != True):
            for k in range(len(list(value))):
                if (list(value))[k] != '':
                    value_list = json.loads((list(value))[k])
                    if len(value_list) != 0:
                        for j in range(len(value_list)):
                            dic = value_list[j]
                            c_date = dic.get('last_time_contacted', '0')
                            if c_date.isdigit() == True:
                                cont_date = int(c_date)
                                if cont_date > date_max:
                                    date_max = cont_date
                            else:
                                date_max = np.NaN
                    else:
                        date_max = np.NaN
        else:
            date_max = np.NaN
        dv_list.append(device_list[index])
        date_diff = int((upd_df['@content@_ep@timestamp'].values)[0]) - date_max
        dv_list.append(date_diff)
        contact_diff.append(dv_list)
    arry_diff = np.array(contact_diff)
    df_diff = pd.DataFrame(arry_diff, columns=['@device_id', 'contacts_diff'])
    for index in range(L):
        upd_df = update_df.loc[update_df['@device_id'] == device_list[index]]
        value = upd_df['@content@_ep@attribute@contacts'].values
        dv_list = []
        Counts = 0
        if np.any(pd.isna(value) != True):
            for k in range(len(list(value))):
                if (list(value))[k]!='':
                    value_list = json.loads((list(value))[k])
                    if len(value_list) != 0:
                       for j in range(len(value_list)):
                           dic = value_list[j]
                           t_count=dic.get('times_contacted','0')
                           if t_count.isdigit==True:
                              count = int(t_count)
                              Counts = Counts + count
                           else:
                              Counts = np.NaN
                    else:
                        Counts = np.NaN
        else:
            Counts = np.NaN
        dv_list.append(device_list[index])
        dv_list.append(Counts)
        contact_count.append(dv_list)
    arry_count = np.array(contact_count)
    df_count = pd.DataFrame(arry_count, columns=['@device_id', 'contacts_count'])
    final_df = pd.merge(df_num, df_count, on='@device_id')
    Final_df = pd.merge(final_df, df_diff, on='@device_id')

    return Final_df
# Final_df = contacts()
# print(Final_df)
def connected_wifi():
    update_df = pd.DataFrame()
    new_df = data2.set_index(['@device_id', '@content@_ep@timestamp'])
    df_conn_wifi = new_df.loc[:, ['@content@_ep@attribute@connect_wifi@ssid']]
    data_list = []
    # for index in range(L):
    #     df_device = df_conn_wifi.loc[[device_list[index]], :]
    #     l = len(df_device)
    #     for i in range(l):
    #         value = df_device.iloc[i, :].values  # value:array
    #
    #         if np.any(pd.isna(value) != True):
    #             for j in range(len(list(value))):
    #                 if (list(value))[j] != '':
    #                     dic = json.loads((list(value))[j])
    #                     if dic['ssid'] != '<unknown ssid>':
    #                         df_device.iloc[i, :] = dic['ssid']
    #                     else:
    #                         df_device.iloc[i, :] = np.NaN
    #
    #         else:
    #             df_device.iloc[i, :] = np.NaN
    #         # if np.any(pd.isna(value) != True):
    #         #     for j in range(len(list(value))):
    #         #         if (list(value))[j] != '':
    #         #             dic = json.loads((list(value))[j])
    #         #             if dic['ssid'] != '<unknown ssid>':
    #         #                 df_device.iloc[i, :] = dic['ssid']
    #         #             else:
    #         #                 df_device.iloc[i, :] = np.NaN
    #
    #         # else:
    #         #     df_device.iloc[i, :] = np.NaN
    #     update_df = update_df.append(df_device)
    for index in range(L):
        dv_list = []
        wf_list = []
        df_update_device = df_conn_wifi.loc[[device_list[index]], :]
        l = len(df_update_device)
        for i in range(l):
            value = df_update_device.iloc[i, :].values
            if np.any(pd.isna(value) != True):
                for j in range(len(list(value))):
                    if (list(value))[j] != '':
                        wf_list.append((list(value))[j])
        wf_list = np.unique(wf_list)
        dv_list.append(device_list[index])
        dv_list.append(len(wf_list))
        data_list.append(dv_list)
    arry = np.array(data_list)
    final_df = pd.DataFrame(arry, columns=['@device_id', 'conn_wifi_num'])
    return final_df
    # for index in range(L):
    #     dv_list = []
    #     wf_list = []
    #     df_update_device = update_df.loc[[device_list[index]], :]
    #     l = len(df_update_device)
    #     for i in range(l):
    #         value = df_update_device.iloc[i, :].values
    #         if np.any(pd.isna(value) != True):
    #             for j in range(len(list(value))):
    #                 wf_list.append((list(value))[j])
    #     wf_list = np.unique(wf_list)
    #     dv_list.append(device_list[index])
    #     dv_list.append(len(wf_list))
    #     data_list.append(dv_list)
    # arry = np.array(data_list)
    # final_df = pd.DataFrame(arry, columns=['@device_id', 'conn_wifi_num'])
    # return final_df
# fina = connected_wifi()
# print(fina)

def wifi_list():
    update_df = pd.DataFrame()
    new_df = data2.set_index(['@device_id', '@content@_ep@timestamp'])
    df_wifi = new_df.loc[:, ['@content@_ep@attribute@wifi_list']]
    data_list = []
    for index in range(L):
        df_device = df_wifi.loc[[device_list[index]], :]
        l = len(df_device)
        dv_set = set([])
        dv_list = []
        for i in range(l):
            wifi_set = set([])
            value = df_device.iloc[i, :].values  # value:array
            if np.any(pd.isna(value) != True):
                for j in range(len(list(value))):
                    if (list(value))[j] != '':
                        wifi_set = set(((list(value))[j]).split('|'))
                        dv_set = dv_set | wifi_set
        dv_list.append(device_list[index])
        dv_list.append(len(dv_set))
        data_list.append(dv_list)
    arry = np.array(data_list)
    final_df = pd.DataFrame(arry, columns=['@device_id', 'wifi_list_num'])
    return final_df
# final_df = wifi_list()
# print(final_df)

def wifi_state():
    update_df = pd.DataFrame()
    new_df = data2.set_index(['@device_id', '@content@_ep@timestamp'])
    df_wifi = new_df.loc[:, ['@content@_ep@attribute@wifi_state']]
    data_list = []
    for index in range(L):
        df_device = df_wifi.loc[[device_list[index]], :]
        l = len(df_device)
        dv_set = set([])
        dv_list = []
        for i in range(l):
            wifi_set = set([])
            value = df_device.iloc[i, :].values  # value:array
            if np.any(pd.isna(value) != True):
                for k in range(len(list(value))):
                    if (list(value))[k] != '':
                        value_list = json.loads((list(value))[k])
                        if len(value_list) != 0:
                            for j in range(len(value_list)):
                                dic = value_list[j]
                                wifi_set.add(dic['ssid'])
                            dv_set = dv_set | wifi_set

        dv_list.append(device_list[index])
        dv_list.append(len(dv_set))
        data_list.append(dv_list)
    arry = np.array(data_list)
    final_df = pd.DataFrame(arry, columns=['@device_id', 'wifi_state_num'])
    return final_df
# fina = wifi_state()
# print(fina)
#fengmin

# print(ped_mean)
# print(ped_varia)
# print(ped_time)


from pandas.core.frame import DataFrame
c = {"@device_id" : div_uni, 'app_key':app_len, 'net':net_change, 'carrier':carrier_change,
     "ped_mean": ped_mean, 'ped_vari':ped_varia,  'ped_time':ped_time, 'abd':adb_adb, 'abd_usb':adb_usb,
     'imsi': imsi_change, 'alarms':alarm_change, 'pn':pn_change,
     'cmdline': cmd_change, 'location_area_code': code_change, 'storage_mean': storage_mean,
     'storage_vari':storage_vari}#将列表a，b转换成字典
cc = DataFrame(c)#将字典转换成为数据框
