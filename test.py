# coding: utf-8
__author__ = "shuxin"
__date__ = "2018/9/21 10:00"

import time
import pandas as pd
import numpy as np


def test():
    names = ['a', 'b', 'c']
    names2 = names.copy()
    names2[0] = 'd'
    print(names)
    print(names2)


# # coding=utf-8
import copy


def test2():
    names = ['fsp', 'hj', 'fm', 'fp']
    name2 = names[:]
    print(names)
    print(name2)
    names[2] = 'lm'
    print(names)
    print(name2)


def test3():
    list_ = ['0', '0', '1', '1']
    rep_list = map(lambda x: 1 if x == 0 else 2, list_)
    print(list(rep_list))


def get_d(d):
    print("11111111", d)


def test4():
    dict = {'key1': ['a', 'a', 'b', 'b', 'c', 'c', 'c'], 'key2': [1, 1, 2, 2, 3, 3, 3]}
    df = pd.DataFrame(dict)
    print(df[(df['key1'] != 'a') & (df['key1'] != 'c')])
    group_size = df.groupby(by='key1').size()
    # print(type(group_size))
    # print((group_size[group_size==2]).count())


def get_list(name, value):
    name = list()
    name.append(value)
    return name


def test5():
    test_dict = dict()
    for i in range(1, 4):
        test_dict['key1'] = 1
        test_dict['key2'] = 3
    print(pd.DataFrame(dict))
    # df=pd.DataFrame(test_dict).reset_index()
    # print(df)
    # df=pd.concat(pd.DataFrame(test_dict)).

    # print(df)


def trends_list(name):  # ,value
    prepare_list = locals()
    prepare_list['list_' + str(name)] = []
    # prepare_list['list_' + str(name)].append(value)
    return prepare_list['list_' + str(name)]


def test6():
    a = [['1', '2', '5'], ['1', '4', '7'], ['2', '5', '6']]
    b = pd.DataFrame(a, columns=['a', 'b', 'c'])
    print(b[(b['a'] == '1') & (b['a'] == '1')])
    for index, row in b.iterrows():
        print(row['a'], row['b'], row['c'])


def to_string(s):
    s.replace('\'', '')
    return s


def test7():
    list1 = ['aa', 'bb', 'cc']
    print(type(str(list1)))


def totime(my_time_str):
    import time
    from datetime import datetime

    time_stamp = int(time.mktime(
        datetime.strptime(str(my_time_str), "%Y-%m-%d %H:%M:%S.%f").timetuple()))
    return time_stamp


def test8():
    df = pd.DataFrame(
        [
            [pd.Timestamp.now()]
        ], columns=['time']
    )

    df['timeint'] = df['time'].apply(totime)
    print(df)


def test9():
    from sympy import Symbol, solve
    x = Symbol('x')
    y = Symbol('y')
    print(solve([y + x - 1, 3 * x + 2 * y - 5], [x, y]))


def test10():
    import matplotlib.pyplot as plt
    import numpy as np
    import math
    def get_tan(x,y):
        return y/x

    def y1(x1):
        return get_tan(1,-1) * x1 #- 1.0028

    # def y2(x2):
    #     return -0.01 * x2 + 4.0028

    x = np.arange(-350, 350, 50)
    y1 = y1(x)
    # y2 = y2(x)
    plt.plot(x, y1)
    # plt.plot(x, y2)

    # plt.xlim&ylim可以限制x轴或者y轴的范围，相当于把图像从某个小区域进行放大，或者从某个更大的区域缩小
    plt.xlim(-350, 350)
    plt.ylim(-350, 350)
    plt.show()



def test11():
    import math
    # print
    # "tan(3) : ", math.tan(3)
    # print
    # "tan(-3) : ", math.tan(-3)
    # print
    # "tan(0) : ", math.tan(0)
    # print
    # "tan(math.pi) : ", math.tan(math.pi)
    # print
    # "tan(math.pi/2) : ", math.tan(math.pi / 2)
    print("tan(math.pi/4) : ", math.tan(math.pi / 4))

