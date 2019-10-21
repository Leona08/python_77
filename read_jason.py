import json as js
import csv
import sys
import importlib
import pandas as pd


def read_list(key, value, parent, ch):
    '''
    Read list that includes lists of dictionaries

    :param key:
    :param value:
    :param parent:
    :param ch:
    :return: a dictionary or a list of dictionaries
    '''
    res_dict = dict()
    res_list = list()
    if len(value) > 0:
        if isinstance(value[0], dict):
            for i in range(len(value)):
                # temp = read_dict(value[i], parent + ch + key + ch + str(i))
                # res = {**res, **temp}
                res_list.append(read_dict(value[i], parent + ch + key, ch))
        else:
            # print(parent + ch + key, value)
            res_dict[parent + ch + key] = value
    return res_dict, res_list


def read_str(key, value, parent, ch):
    '''
    Read string that includes dictionary or list

    :param key:
    :param value:
    :param parent:
    :param ch:
    :return: a dictionary
    '''
    res = dict()
    if len(value) > 0:
        value = value.replace('true', 'True')
        value = value.replace('false', 'False')
        if value[0] == '[' and value[-1] == ']':
            try:
                temp = read_list(key, eval(value), parent, ch)
                res = {**res, **temp}
            except:
                res[parent + ch + key] = value
        elif value[0] == '{' and value[-1] == '}':
            try:
                temp = read_dict(eval(value), parent + ch + key, ch)
                res = {**res, **temp}
            except:
                res[parent + ch + key] = value
        else:
            # print(parent + ch + key, value)
            res[parent + ch + key] = value
    else:
        # print(parent + ch + key, value)
        res[parent + ch + key] = value
    return res


def read_dict(cur_line, parent, ch):
    '''
    Read nested dictionaries

    :param cur_line: a line in the file
    :param parent: the name of parent
    :param ch: the separate characters
    :return: a list of dictionaries
    '''
    res = dict()
    for key, value in cur_line.items():
        if isinstance(value, dict):
            temp = read_dict(value, parent + ch + key, ch)
            res = {**res, **temp}
        elif isinstance(value, list):
            temp_dict, temp_list = read_list(key, value, parent, ch)
            if len(temp_dict) > 0:
                res = {**res, **temp_dict}
            if len(temp_list) > 0:
                res_list.append(temp_list)
        elif isinstance(value, str):
            temp = read_str(key, value, parent, ch)
            res = {**res, **temp}
        else:
            # print(parent + ch + key, value)
            res[parent + ch + key] = value
    return res


# convert jason to DataFrame
f = open('/Users/fengminwu/Documents/PycharmProjects/python/data_V001_android_201801_02_08_1_1514694388278.json', encoding='UTF-8')
count = 0
data_list = list()
res_list = list()
line = f.readline()
while line:
    data = js.loads(line)
    res_list = list()
    ress = read_dict(data, parent='', ch='@')

    if len(res_list) > 1:
        print("--- More than one list ")
    final_res = list()
    for i in range(len(res_list[0])):
        final_res.append({**res_list[0][i], **ress})
    data_list += final_res

    line = f.readline()

    if count % 1000 == 0:
        print(" ----- %d -------" % count)
    count += 1
f.close()
data_df = pd.DataFrame(data_list)
print(data_df.shape)
print(data_df['@content@_cp@carrier'].unique())
for i in range(len(data_df)):
    if data_df.loc[i, '@content@_ep@attribute@alarms'] == '':
        print('the value is null')
    if pd.isna(data_df.loc[i, '@content@_ep@attribute@alarms']):
        print('the value is none')
#     if pd.isna(data_df.loc[i, '@content@_ep@net']) == True:
#         print('null')
# len(data_df) == len(data_df['@content@_ep@attribute@alarms'])
data_df['@content@_ep@attribute@alarms'].unique()


data_df['@content@_cp@carrier'].info()
# data_df.head(200).to_csv("C:/Users/zhang/Documents/zxhang/my Data/学校/学生管理/毕业设计/博士/"
#                "余江尼/实验/data.csv")


# # testing
# x = {'x1': 2, 'x2': 345, 'x3':[{'x1': 789, 'x2': 456}, {'x1':'456', 'x2': 235, 'x3': 99}],
#      'x4': [1, 2, 3], 'x5': 'er|ert|abc', 'x6': {'x3': 22, 'x4': 'ert'}, 'x7': '[4,4]',
#      'x8': "{'x3':4, 'x5':'rr'}", 'x10': '[hello]',
#      'x9': {'y1':{'y2':3, 'y3':45}, 'y5': [{'x6': 56, 'x9': 88}, {'x6': 44, 'x9': 668}]}}
# res_list = list()
# ress = read_dict(x)
#
# final_res = list()
# for i in range(len(res_list[0])):
#     final_res.append({**ress, **res_list[0][i]})
# ss = pd.DataFrame(final_res)
