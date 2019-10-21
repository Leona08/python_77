import json
import pandas as pd
import numpy as np
df=pd.read_csv('df.csv',encoding = 'utf-8')
device_list=list(set(df['device_id']))
L=len(device_list)
def battery():
    new_df = df.set_index(['device_id', 'timestamp'])
    df_battery=new_df.loc[:,['battery']]
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
                    if (list(value))[j]!='':
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
    df_mean = pd.DataFrame(arry_mean, columns=['device_id', 'battery_mean'])
    for index in range(L):
        dv_list = []
        df_update_device = update_df.loc[[device_list[index]], :]
        var = float(df_update_device.var())
        dv_list.append(device_list[index])
        dv_list.append(var)
        data_var.append(dv_list)
    arry_var = np.array(data_var)
    df_var = pd.DataFrame(arry_var, columns=['device_id', 'battery_var'])
    final_df = pd.merge(df_mean, df_var, on='device_id')
    return final_df

def call():
    update_df = pd.DataFrame()
    new_df = df
    df_call = new_df.loc[:, ['device_id', 'timestamp', 'call']]
    call_num = []
    call_dur = []
    call_diff = []
    for index in range(L):
        df_device = df_call.loc[df_call['device_id'] == device_list[index]]
        df_device = df_device.loc[df_device['timestamp'] == df_device['timestamp'].max()]
        update_df = update_df.append(df_device)
    for index in range(L):
        upd_df = update_df.loc[update_df['device_id'] == device_list[index]]
        value = upd_df['call'].values
        dv_list = []
        counts=0
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
    df_num = pd.DataFrame(arry_num, columns=['device_id', 'call_num'])
    for index in range(L):
        upd_df = update_df.loc[update_df['device_id'] == device_list[index]]
        value = upd_df['call'].values
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
        date_diff = int((upd_df['timestamp'].values)[0]) - date_max
        dv_list.append(date_diff)
        call_diff.append(dv_list)
    arry_diff = np.array(call_diff)
    df_diff = pd.DataFrame(arry_diff, columns=['device_id', 'call_diff'])
    for index in range(L):
        upd_df = update_df.loc[update_df['device_id'] == device_list[index]]
        value = upd_df['call'].values
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
    df_dur = pd.DataFrame(arry_dur, columns=['device_id', 'call_duration'])
    final_df = pd.merge(df_num, df_dur, on='device_id')
    Final_df = pd.merge(final_df, df_diff, on='device_id')
    return Final_df

def message():
    update_df = pd.DataFrame()
    new_df = df
    df_msg = new_df.loc[:, ['device_id', 'timestamp', 'message']]
    msg_num = []
    msg_diff = []
    for index in range(L):
        df_device = df_msg.loc[df_msg['device_id'] == device_list[index]]
        df_device = df_device.loc[df_device['timestamp'] == df_device['timestamp'].max()]
        update_df = update_df.append(df_device)
    for index in range(L):
        upd_df = update_df.loc[update_df['device_id'] == device_list[index]]
        value = upd_df['message'].values
        dv_list = []
        counts=0
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
    df_num = pd.DataFrame(arry_num, columns=['device_id', 'message_num'])
    for index in range(L):
        upd_df = update_df.loc[update_df['device_id'] == device_list[index]]
        value = upd_df['message'].values
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
        date_diff = int((upd_df['timestamp'].values)[0]) - date_max
        dv_list.append(date_diff)
        msg_diff.append(dv_list)
    arry_diff = np.array(msg_diff)
    df_diff = pd.DataFrame(arry_diff, columns=['device_id', 'message_diff'])
    final_df = pd.merge(df_num, df_diff, on='device_id')
    return final_df
def photo():
    update_df = pd.DataFrame()
    new_df = df
    df_photo = new_df.loc[:, ['device_id', 'timestamp', 'photo']]
    photo_num = []
    photo_diff = []
    for index in range(L):
        df_device = df_photo.loc[df_photo['device_id'] == device_list[index]]
        df_device = df_device.loc[df_device['timestamp'] == df_device['timestamp'].max()]
        update_df = update_df.append(df_device)

    for index in range(L):
        upd_df = update_df.loc[update_df['device_id'] == device_list[index]]
        value = upd_df['photo'].values
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
    df_num = pd.DataFrame(arry_num, columns=['device_id', 'photo_num'])

    for index in range(L):
        upd_df = update_df.loc[update_df['device_id'] == device_list[index]]
        value = upd_df['photo'].values
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
        date_time = int((upd_df['timestamp'].values)[0])
        date_diff = date_time - date_max
        dv_list.append(date_diff)
        photo_diff.append(dv_list)
    arry_diff = np.array(photo_diff)
    df_diff = pd.DataFrame(arry_diff, columns=['device_id', 'photo_diff'])
    final_df = pd.merge(df_num, df_diff, on='device_id')
    return final_df
def contacts():
    update_df = pd.DataFrame()
    new_df = df
    df_contact = new_df.loc[:, ['device_id', 'timestamp', 'contacts']]
    contact_num = []#联系人数
    contact_diff = []
    contact_count = []  # 累计联系次数
    for index in range(L):
        df_device = df_contact.loc[df_contact['device_id'] == device_list[index]]
        df_device = df_device.loc[df_device['timestamp'] == df_device['timestamp'].max()]
        update_df = update_df.append(df_device)
    for index in range(L):
        upd_df = update_df.loc[update_df['device_id'] == device_list[index]]
        value = upd_df['contacts'].values
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
    df_num = pd.DataFrame(arry_num, columns=['device_id', 'contacts_num'])
    for index in range(L):
        upd_df = update_df.loc[update_df['device_id'] == device_list[index]]
        value = upd_df['contacts'].values
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
        date_diff = int((upd_df['timestamp'].values)[0]) - date_max
        dv_list.append(date_diff)
        contact_diff.append(dv_list)
    arry_diff = np.array(contact_diff)
    df_diff = pd.DataFrame(arry_diff, columns=['device_id', 'contacts_diff'])
    for index in range(L):
        upd_df = update_df.loc[update_df['device_id'] == device_list[index]]
        value = upd_df['contacts'].values
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
    df_count = pd.DataFrame(arry_count, columns=['device_id', 'contacts_count'])
    final_df = pd.merge(df_num, df_count, on='device_id')
    Final_df = pd.merge(final_df, df_diff, on='device_id')

    return Final_df
def connected_wifi():
    update_df = pd.DataFrame()
    new_df = df.set_index(['device_id', 'timestamp'])
    df_conn_wifi = new_df.loc[:, ['connect_wifi']]
    data_list = []
    for index in range(L):
        df_device = df_conn_wifi.loc[[device_list[index]], :]
        l = len(df_device)
        for i in range(l):
            value = df_device.iloc[i, :].values  # value:array
            if np.any(pd.isna(value) != True):
                for j in range(len(list(value))):
                    if (list(value))[j]!='':
                        dic = json.loads((list(value))[j])
                        if dic['ssid'] != '<unknown ssid>':
                           df_device.iloc[i, :] = dic['ssid']
                        else:
                           df_device.iloc[i, :] = np.NaN

            else:
                df_device.iloc[i, :] = np.NaN
        update_df = update_df.append(df_device)
    for index in range(L):
        dv_list = []
        wf_list = []
        df_update_device = update_df.loc[[device_list[index]], :]
        l = len(df_update_device)
        for i in range(l):
            value = df_update_device.iloc[i, :].values
            if np.any(pd.isna(value) != True):
                for j in range(len(list(value))):
                    wf_list.append((list(value))[j])
        wf_list = np.unique(wf_list)
        dv_list.append(device_list[index])
        dv_list.append(len(wf_list))
        data_list.append(dv_list)
    arry = np.array(data_list)
    final_df = pd.DataFrame(arry, columns=['device_id', 'conn_wifi_num'])
    return final_df
def wifi_list():
    update_df = pd.DataFrame()
    new_df = df.set_index(['device_id', 'timestamp'])
    df_wifi = new_df.loc[:, ['wifi_list']]
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
                    if (list(value))[j]!='':
                        wifi_set = set(((list(value))[j]).split('|'))
                        dv_set = dv_set | wifi_set
        dv_list.append(device_list[index])
        dv_list.append(len(dv_set))
        data_list.append(dv_list)
    arry = np.array(data_list)
    final_df = pd.DataFrame(arry, columns=['device_id', 'wifi_list_num'])
    return final_df
def wifi_state():
    update_df = pd.DataFrame()
    new_df = df.set_index(['device_id', 'timestamp'])
    df_wifi = new_df.loc[:, ['wifi_state']]
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
                    if (list(value))[k]!='':
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
    final_df = pd.DataFrame(arry, columns=['device_id', 'wifi_state_num'])
    return final_df
