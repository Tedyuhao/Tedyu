import xlrd
import matplotlib.pyplot as plt


def oneday_sp(path=r'C:\Users\Ted\Desktop\地面观测数据',place='徐州', date='2009/02/20'):
    """画出data日的本站气压随时间变化的折线图"""

    file = path + '\\' + place + '.xls'
    wb = xlrd.open_workbook(filename=file)  # 打开文件
    sheet1 = wb.sheet_by_name('气压')  # 通过名字获取表格
    times = sheet1.col_values(0)
    del times[0]
    i=0
    xuhao={}
    for key in times:
        xuhao[key] = i
        i = i+1
    date_0 = date + ' 00时'
    start = xuhao[date_0]
    the_times = times[start:start + 24]
    station_pressures = sheet1.col_values(1)
    del station_pressures[0]
    i = 0
    for s in station_pressures:
        if float(s) < 100:
            s += 1000
            station_pressures[i] = s
        i = i + 1
    the_sp0 = station_pressures[start:start + 24]
    plt.figure(figsize=(8,4))  # 创建绘图对象
    plt.plot(the_times,the_sp0,"b--",linewidth=1)  # 在当前绘图对象绘图，蓝色虚线，宽线度
    plt.xlabel("Time")
    plt.ylabel("气压")
    plt.title(date + "日气压变化情况")
    plt.xticks(rotation=-90)
    plt.rcParams['font.sans-serif']=['SimHei']

    plt.show()


def lowest_pressure(path=r'C:\Users\Ted\Desktop\地面观测数据',place='徐州',month='2009/12'):
    """画出month月的本站日最低气压随时间变化的折线图"""

    file = path + '\\' + place + '.xls'
    wb = xlrd.open_workbook(filename=file)  # 打开文件
    sheet1 = wb.sheet_by_name('气压')  # 通过名字获取表格
    shuju = sheet1.col_values(0)
    del shuju[0]
    times = []
    i = 0
    while i<len(shuju):
        zhi = shuju[i]
        times.append(zhi[0:10])
        i = i+24
    shuju2 = sheet1.col_values(4)
    del shuju2[0]
    lps = []
    for lp in shuju2:
        if len(str(lp)) > 0:
            if lp < 100:
                lp = lp + 1000
            lps.append(lp)
    xuhao = {}
    i = 0
    for time in times:
        xuhao[time] = i
        i = i + 1
    data_1 = str(month) + '/1 '
    num = xuhao[data_1]
    yue = {}
    yue['2009/01'] = 31
    yue['2009/02'] = 28
    yue['2009/03'] = 31
    yue['2009/04'] = 30
    yue['2009/05'] = 31
    yue['2009/06'] = 30
    yue['2009/07'] = 31
    yue['2009/08'] = 31
    yue['2009/09'] = 30
    yue['2009/10'] = 31
    yue['2009/11'] = 30
    yue['2009/12'] = 31
    yue['2010/01'] = 31
    yue['2010/02'] = 28
    yue['2010/03'] = 31
    yue['2010/04'] = 30
    yue['2010/05'] = 31
    yue['2010/06'] = 30
    yue['2010/07'] = 31
    yue['2010/08'] = 31
    yue['2010/09'] = 30
    yue['2010/10'] = 31
    yue['2010/11'] = 30
    yue['2010/12'] = 31
    the_times = times[num:num+yue[month]]
    the_lp = lps[num:num+yue[month]]
    plt.figure(figsize=(11,5))  # 创建绘图对象
    plt.plot(the_times,the_lp,"b--",linewidth=1)  # 在当前绘图对象绘图，蓝色虚线，宽线度
    plt.xlabel("Time")
    plt.ylabel("日最低气压")
    plt.xticks(rotation=-90)
    plt.rcParams['font.sans-serif']=['SimHei']
    plt.show()


def highest_pressure(path=r'C:\Users\Ted\Desktop\地面观测数据',place='徐州',month='2009/06',contrast= False,t=False):
    """画出month月的本站日最高气压随时间变化的折线图,当contrast=True时，不进行绘图，只返回相应月份最高气压列表"""

    file = path + '\\' + place +'.xls'
    wb = xlrd.open_workbook(filename=file)  # 打开文件
    sheet1 = wb.sheet_by_name('气压')  # 通过名字获取表格

    shuju = sheet1.col_values(0)  # 用shuju获取第0列的全部包含空行的数据
    del shuju[0:4]  # 删除第一个元素‘时间’
    times = []
    i = 0
    while i<len(shuju):
        zhi = shuju[i]
        times.append(zhi[0:10])
        i = i+24
    shuju2 = sheet1.col_values(2)
    del shuju2[0]
    hps = []  # 用hps存储 “日最高气压”
    for hp in shuju2:
        if len(str(hp)) > 0:
            if hp < 100:
                hp = hp + 1000
            hps.append(hp)
    xuhao = {}
    i = 0
    for time in times:
        xuhao[time] = i
        i = i + 1
    data_1 = str(month) + '/1 '
    num = xuhao[data_1]
    yue = {}
    yue['2009/01'] = 31
    yue['2009/02'] = 28
    yue['2009/03'] = 31
    yue['2009/04'] = 30
    yue['2009/05'] = 31
    yue['2009/06'] = 30
    yue['2009/07'] = 31
    yue['2009/08'] = 31
    yue['2009/09'] = 30
    yue['2009/10'] = 31
    yue['2009/11'] = 30
    yue['2009/12'] = 31
    yue['2010/01'] = 31
    yue['2010/02'] = 28
    yue['2010/03'] = 31
    yue['2010/04'] = 30
    yue['2010/05'] = 31
    yue['2010/06'] = 30
    yue['2010/07'] = 31
    yue['2010/08'] = 31
    yue['2010/09'] = 30
    yue['2010/10'] = 31
    yue['2010/11'] = 30
    yue['2010/12'] = 31
    the_times = times[num:num+yue[month]]
    the_hp = hps[num:num+yue[month]]
    if contrast:
        if t:
            return the_times
        return the_hp
    plt.figure(figsize=(8,4))#创建绘图对象
    plt.plot(the_times,the_hp,"b--",linewidth=1)#在当前绘图对象绘图，蓝色虚线，宽线度
    plt.xlabel("Time")
    plt.ylabel('日最高气压')
    plt.title(month + '月  日最高气压变化情况')
    plt.xticks(rotation=-90)
    plt.rcParams['font.sans-serif']=['SimHei']

    fig, (ax0, ax1) = plt.subplots(nrows=2, figsize=(9, 6))
    ax0.hist(the_hp, 30, density=1, histtype='bar', facecolor='yellowgreen', alpha=0.75)
    ax0.set_title(month + '月  日最高气压 概率分布直方图')
    ax1.hist(the_hp, 30, density=1, histtype='bar', facecolor='pink', alpha=0.75, cumulative=True, rwidth=0.8)
    ax1.set_title(month + '月  日最高气压 累计概率分布')
    plt.rcParams['font.sans-serif'] = ['SimHei']

    plt.show()


def h_p_contrast(path=r'C:\Users\Ted\Desktop\地面观测数据',month='2009/06',):
    """对三地的日最高气压进行对比分析"""

    fengxian = highest_pressure(path=path, place='徐州', month=month, contrast=True)
    peixian = highest_pressure(path=path, place='沛县', month=month, contrast=True)
    xuzhou = highest_pressure(path=path, place='丰县', month=month, contrast=True)
    the_times = highest_pressure(path=path, place='徐州', month=month, contrast=True, t=True)
    fig,ax = plt.subplots()
    ax.plot(the_times, fengxian, label='丰县')
    ax.plot(the_times, peixian, label='沛县')
    ax.plot(the_times, xuzhou, label='徐州')
    ax.set(ylabel='atmospheric pressure(hPa)', xlabel='Time', title='日最高气压对比')
    ax.legend()
    plt.xticks(rotation=-90)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.show()


def highest_temperature(path=r'C:\Users\Ted\Desktop\地面观测数据',place='徐州',month='2009/06',contrast=False,t=False):
    """画出month月的本站日最高气温随时间变化的折线图，概率分布直方图和累计概率分布图"""

    file = path + '\\' + place + '.xls'
    wb = xlrd.open_workbook(filename=file)  # 打开文件
    sheet1 = wb.sheet_by_name('气温')  # 通过名字获取表格

    shuju = sheet1.col_values(0)  # 用shuju获取第0列的全部包含空行的数据
    del shuju[0:4]  # 删除第一个元素‘时间’

    times = []  # 存储非空数据
    i = 0
    while i < len(shuju):
        zhi = shuju[i]
        times.append(zhi[0:10])
        i = i+24
    shuju2 = sheet1.col_values(2)
    del shuju2[0]
    hts = []  # 用hps存储 “日最高气温”
    for ht in shuju2:
        if len(str(ht)) > 0:
            hts.append(ht)
    xuhao = {}
    i = 0
    for time in times:
        xuhao[time] = i
        i = i + 1

    data_1 = str(month) + '/1 '
    num = xuhao[data_1]
    yue = {}
    yue['2009/01'] = 31
    yue['2009/02'] = 28
    yue['2009/03'] = 31
    yue['2009/04'] = 30
    yue['2009/05'] = 31
    yue['2009/06'] = 30
    yue['2009/07'] = 31
    yue['2009/08'] = 31
    yue['2009/09'] = 30
    yue['2009/10'] = 31
    yue['2009/11'] = 30
    yue['2009/12'] = 31
    yue['2010/01'] = 31
    yue['2010/02'] = 28
    yue['2010/03'] = 31
    yue['2010/04'] = 30
    yue['2010/05'] = 31
    yue['2010/06'] = 30
    yue['2010/07'] = 31
    yue['2010/08'] = 31
    yue['2010/09'] = 30
    yue['2010/10'] = 31
    yue['2010/11'] = 30
    yue['2010/12'] = 31
    the_times = times[num:num+yue[month]]
    the_hp = hts[num:num+yue[month]]
    if contrast:
        if t:
            return the_times
        return the_hp
    plt.figure(figsize=(8,4))  # 创建绘图对象
    plt.plot(the_times,the_hp,"b--",linewidth=1)  # 在当前绘图对象绘图，蓝色虚线，宽线度
    plt.xlabel("Time")
    plt.ylabel('日最高气温')
    plt.title(month+'月  日最高气温变化情况')
    plt.xticks(rotation=-90)
    plt.rcParams['font.sans-serif']=['SimHei']

    fig, (ax0, ax1) = plt.subplots(nrows=2, figsize=(9, 6))
    ax0.hist(the_hp, 30, density=1, histtype='bar', facecolor='yellowgreen', alpha=0.75)
    ax0.set_title(month + '月  日最高气温 概率分布直方图')
    ax1.hist(the_hp, 30, density=1, histtype='bar', facecolor='pink', alpha=0.75, cumulative=True, rwidth=0.8)
    ax1.set_title(month + '月  日最高气温 累计概率分布')
    plt.rcParams['font.sans-serif'] = ['SimHei']

    plt.show()


def lowest_temperature(path=r'C:\Users\Ted\Desktop\地面观测数据',place='徐州',month='2009/06'):
    """画出month月的本站日最低气温随时间变化的折线图"""

    file = path + '\\' + place + '.xls'
    wb = xlrd.open_workbook(filename=file)  # 打开文件
    sheet1 = wb.sheet_by_name('气温')  # 通过名字获取表格

    shuju = sheet1.col_values(0)  # 用shuju获取第3列的全部包含空行的数据
    del shuju[0:4]  # 删除第一个元素‘时间’

    times = []
    i = 0
    while i < len(shuju):
        zhi = shuju[i]
        times.append(zhi[0:10])
        i = i+24
    shuju2 = sheet1.col_values(4)
    del shuju2[0]
    hts = []  # 用hps存储 “日最高气温”
    for ht in shuju2:
        if len(str(ht)) > 0:
            hts.append(ht)
    xuhao = {}
    i = 0
    for time in times:
        xuhao[time] = i
        i = i + 1
    data_1 = str(month) + '/1 '
    num = xuhao[data_1]
    yue = {}
    yue['2009/01'] = 31
    yue['2009/02'] = 28
    yue['2009/03'] = 31
    yue['2009/04'] = 30
    yue['2009/05'] = 31
    yue['2009/06'] = 30
    yue['2009/07'] = 31
    yue['2009/08'] = 31
    yue['2009/09'] = 30
    yue['2009/10'] = 31
    yue['2009/11'] = 30
    yue['2009/12'] = 31
    yue['2010/01'] = 31
    yue['2010/02'] = 28
    yue['2010/03'] = 31
    yue['2010/04'] = 30
    yue['2010/05'] = 31
    yue['2010/06'] = 30
    yue['2010/07'] = 31
    yue['2010/08'] = 31
    yue['2010/09'] = 30
    yue['2010/10'] = 31
    yue['2010/11'] = 30
    yue['2010/12'] = 31
    the_times = times[num:num+yue[month]]
    the_hp = hts[num:num+yue[month]]
    plt.figure(figsize=(8,4))  # 创建绘图对象
    plt.plot(the_times,the_hp,"b--",linewidth=1)  # 在当前绘图对象绘图，蓝色虚线，宽线度
    plt.xlabel("Time")
    plt.ylabel('日最高气温')
    plt.title(month+'月  日最低气温变化情况')
    plt.xticks(rotation=-90)
    plt.rcParams['font.sans-serif']=['SimHei']

    fig, (ax0, ax1) = plt.subplots(nrows=2, figsize=(9, 6))
    ax0.hist(the_hp, 30,density=1, histtype='bar', facecolor='yellowgreen', alpha=0.75)
    ax0.set_title(month + '月  日最低气温 概率分布直方图')
    ax1.hist(the_hp, 30,density=1, histtype='bar', facecolor='pink', alpha=0.75, cumulative=True, rwidth=0.8)
    ax1.set_title(month + '月  日最低气温 累计概率分布')

    plt.show()


def oneday_temp(path=r'C:\Users\Ted\Desktop\地面观测数据',place='徐州', date='2009/01/1'):
    """画出data日的本站气温随时间变化的折线图"""

    file = path + '\\' + place + '.xls'
    wb = xlrd.open_workbook(filename=file)#打开文件
    sheet1 = wb.sheet_by_name('气温')#通过名字获取表格
    times = sheet1.col_values(0)#用times获取第0列的全部时间
    del times[0]#删除第一个元素‘时间’
    i=0
    xuhao={}
    for key in times:
        xuhao[key] = i
        i = i+1
    date_0 = date + ' 00时'
    start = xuhao[date_0]
    the_times = times[start:start + 24]
    station_pressures = sheet1.col_values(1)
    del station_pressures[0]
    the_sp0 = station_pressures[start:start + 24]
    plt.figure(figsize=(8,4))  # 创建绘图对象
    plt.plot(the_times,the_sp0,"b--",linewidth=1)  # 在当前绘图对象绘图，蓝色虚线，宽线度
    plt.xlabel("Time")
    plt.ylabel('温度')
    plt.xticks(rotation=-90)
    plt.rcParams['font.sans-serif']=['SimHei']
    plt.title(date + "日气温变化情况")
    plt.rcParams['axes.unicode_minus'] = False  # 解决图像负号显示为方框的问题

    plt.show()


def h_t_contrast(path=r'C:\Users\Ted\Desktop\地面观测数据',month='2009/06'):
    """对三地的日最高气温进行对比分析"""

    fengxian = highest_temperature(path=path, place='徐州', month=month, contrast=True)
    peixian = highest_temperature(path=path, place='沛县', month=month, contrast=True)
    xuzhou = highest_temperature(path=path, place='丰县', month=month, contrast=True)
    the_times = highest_temperature(path=path, place='徐州', month=month, contrast=True, t=True)
    fig,ax = plt.subplots()
    ax.plot(the_times,fengxian,label='丰县')
    ax.plot(the_times,peixian,label='沛县')
    ax.plot(the_times,xuzhou,label='徐州')
    ax.set(ylabel='Air temperature（℃）', xlabel='Time', title='日最高气温对比')
    ax.legend()
    plt.xticks(rotation=-90)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.show()


def g_t(path=r'C:\Users\Ted\Desktop\地面观测数据',place='徐州', date='2009/01/30'):
    """画出data日的本站地温随时间变化的折线图"""

    file = path + '\\' + place + '.xls'
    wb = xlrd.open_workbook(filename=file)
    sheet1 = wb.sheet_by_name('浅层地温')
    times = sheet1.col_values(0)
    del times[0]
    i = 0
    xuhao = {}
    for key in times:
        xuhao[key] = i
        i = i+1
    date_0 = date + ' 00时'
    start = xuhao[date_0]
    the_times = times[start:start + 24]
    station_pressures = sheet1.col_values(1)
    del station_pressures[0]
    the_sp0 = station_pressures[start:start + 24]
    station_pressures = sheet1.col_values(7)
    del station_pressures[0]
    the_sp1 = station_pressures[start:start+24]
    station_pressures = sheet1.col_values(9)
    del station_pressures[0]
    the_sp2 = station_pressures[start:start+24]
    station_pressures = sheet1.col_values(11)
    del station_pressures[0]
    the_sp3 = station_pressures[start:start+24]
    fig, ax = plt.subplots()
    ax.plot(the_times, the_sp0, label='0cm段地温（℃）')
    ax.plot(the_times, the_sp1, label='5cm段地温（℃）')
    ax.plot(the_times, the_sp2, label='15cm段地温（℃）')
    ax.plot(the_times, the_sp3, label='20cm段地温（℃）')
    ax.set(ylabel='ground temperature（℃）', xlabel='Time', title='24小时地温变化')
    ax.legend()
    plt.xticks(rotation=-90)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.show()


def l_g_t(path=r'C:\Users\Ted\Desktop\地面观测数据', place='徐州', month='2009/06', contrast= False,t=False):
    """画出month月的本站0cm段最低地温随时间变化的折线图和概率分布图,当contrast=True时，不进行绘图，只返回相应月份最高气压列表"""

    file = path + '\\' + place + '.xls'
    wb = xlrd.open_workbook(filename=file)  # 打开文件
    sheet1 = wb.sheet_by_name('浅层地温')  # 通过名字获取表格
    shuju = sheet1.col_values(0)  # 用shuju获取第0列的全部包含空行的数据
    del shuju[0:4]  # 删除第一个元素‘时间’
    times = []
    i = 0
    while i<len(shuju):
        zhi = shuju[i]
        times.append(zhi[0:10])
        i = i+24
    shuju2 = sheet1.col_values(4)
    del shuju2[0]
    hps = []
    for hp in shuju2:
        if len(str(hp)) > 0:

            hps.append(hp)
    xuhao = {}
    i = 0
    for time in times:
        xuhao[time] = i
        i = i + 1
    data_1 = str(month) + '/1 '
    num = xuhao[data_1]
    yue = {}
    yue['2009/01'] = 31
    yue['2009/02'] = 28
    yue['2009/03'] = 31
    yue['2009/04'] = 30
    yue['2009/05'] = 31
    yue['2009/06'] = 30
    yue['2009/07'] = 31
    yue['2009/08'] = 31
    yue['2009/09'] = 30
    yue['2009/10'] = 31
    yue['2009/11'] = 30
    yue['2009/12'] = 31
    yue['2010/01'] = 31
    yue['2010/02'] = 28
    yue['2010/03'] = 31
    yue['2010/04'] = 30
    yue['2010/05'] = 31
    yue['2010/06'] = 30
    yue['2010/07'] = 31
    yue['2010/08'] = 31
    yue['2010/09'] = 30
    yue['2010/10'] = 31
    yue['2010/11'] = 30
    yue['2010/12'] = 31
    the_times = times[num:num+yue[month]]
    the_hp = hps[num:num+yue[month]]
    if contrast:
        if t:
            return the_times
        return the_hp
    plt.figure(figsize=(8,4))#创建绘图对象
    plt.plot(the_times,the_hp,"b--",linewidth=1)#在当前绘图对象绘图，蓝色虚线，宽线度
    plt.xlabel("Time")
    plt.ylabel('0cm段最低地温')
    plt.title(month + '月  0cm段最低地温变化情况')
    plt.xticks(rotation=-90)
    plt.rcParams['font.sans-serif']=['SimHei']

    fig, (ax0, ax1) = plt.subplots(nrows=2, figsize=(9, 6))
    ax0.hist(the_hp, 30, density=1, histtype='bar', facecolor='yellowgreen', alpha=0.75)
    ax0.set_title(month + '月  0cm段最低地温 概率分布直方图')
    ax1.hist(the_hp, 30, density=1, histtype='bar', facecolor='pink', alpha=0.75, cumulative=True, rwidth=0.8)
    ax1.set_title(month + '月  0cm段最低地温 累计概率分布')
    plt.rcParams['font.sans-serif'] = ['SimHei']

    plt.show()


def h_g_t(path=r'C:\Users\Ted\Desktop\地面观测数据', place='徐州', month='2009/06', contrast= False,t=False):
    """画出month月的本站0cm段最高地温随时间变化的折线图和概率分布图,当contrast=True时，不进行绘图，只返回相应月份最高气压列表"""

    file = path + '\\' + place + '.xls'
    wb = xlrd.open_workbook(filename=file)  # 打开文件
    sheet1 = wb.sheet_by_name('浅层地温')  # 通过名字获取表格
    shuju = sheet1.col_values(0)  # 用shuju获取第0列的全部包含空行的数据
    del shuju[0:4]  # 删除第一个元素‘时间’
    times = []
    i = 0
    while i<len(shuju):
        zhi = shuju[i]
        times.append(zhi[0:10])
        i = i+24
    shuju2 = sheet1.col_values(2)
    del shuju2[0]
    hps = []
    for hp in shuju2:
        if len(str(hp)) > 0:

            hps.append(hp)
    xuhao = {}
    i = 0
    for time in times:
        xuhao[time] = i
        i = i + 1
    data_1 = str(month) + '/1 '
    num = xuhao[data_1]
    yue = {}
    yue['2009/01'] = 31
    yue['2009/02'] = 28
    yue['2009/03'] = 31
    yue['2009/04'] = 30
    yue['2009/05'] = 31
    yue['2009/06'] = 30
    yue['2009/07'] = 31
    yue['2009/08'] = 31
    yue['2009/09'] = 30
    yue['2009/10'] = 31
    yue['2009/11'] = 30
    yue['2009/12'] = 31
    yue['2010/01'] = 31
    yue['2010/02'] = 28
    yue['2010/03'] = 31
    yue['2010/04'] = 30
    yue['2010/05'] = 31
    yue['2010/06'] = 30
    yue['2010/07'] = 31
    yue['2010/08'] = 31
    yue['2010/09'] = 30
    yue['2010/10'] = 31
    yue['2010/11'] = 30
    yue['2010/12'] = 31
    the_times = times[num:num+yue[month]]
    the_hp = hps[num:num+yue[month]]
    if contrast:
        if t:
            return the_times
        return the_hp
    plt.figure(figsize=(8,4))#创建绘图对象
    plt.plot(the_times,the_hp,"b--",linewidth=1)#在当前绘图对象绘图，蓝色虚线，宽线度
    plt.xlabel("Time")
    plt.ylabel('0cm段最高地温')
    plt.title(month + '月  0cm段最高地温变化情况')
    plt.xticks(rotation=-90)
    plt.rcParams['font.sans-serif']=['SimHei']

    fig, (ax0, ax1) = plt.subplots(nrows=2, figsize=(9, 6))
    ax0.hist(the_hp, 30, density=1, histtype='bar', facecolor='yellowgreen', alpha=0.75)
    ax0.set_title(month + '月  0cm段最高地温 概率分布直方图')
    ax1.hist(the_hp, 30, density=1, histtype='bar', facecolor='pink', alpha=0.75, cumulative=True, rwidth=0.8)
    ax1.set_title(month + '月  0cm段最高地温 累计概率分布')
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.show()


def oneday_hm(path=r'C:\Users\Ted\Desktop\地面观测数据', place='徐州', date='2009/02/30'):
    """画出data日的本站相对湿度随时间变化的折线图"""

    file = path + '\\' + place + '.xls'
    wb = xlrd.open_workbook(filename=file)
    sheet1 = wb.sheet_by_name('相对湿度')#通过名字获取表格
    times = sheet1.col_values(0)#用times获取第0列的全部时间
    del times[0]#删除第一个元素‘时间’
    i = 0
    xuhao={}
    for key in times:
        xuhao[key] = i
        i = i+1
    date_0 = date + ' 00时'
    start = xuhao[date_0]
    the_times = times[start:start + 24]
    station_pressures = sheet1.col_values(1)
    del station_pressures[0]
    the_sp0 = station_pressures[start:start + 24]
    plt.figure(figsize=(8,4))  # 创建绘图对象
    plt.plot(the_times, the_sp0, "b--", linewidth=1)  # 在当前绘图对象绘图，蓝色虚线，宽线度
    plt.xlabel("Time")
    plt.ylabel("相对湿度（%）")
    plt.title(date +"日相对湿度变化情况")
    plt.xticks(rotation=-90)
    plt.rcParams['font.sans-serif']=['SimHei']
    plt.show()


def lowest_humidity(path=r'C:\Users\Ted\Desktop\地面观测数据', place='徐州',month='2009/06',contrast= False,t=False):
    """画出month月的本站日最低相对湿度随时间变化的折线图,当contrast=True时，不进行绘图，只返回相应月份最高气压列表"""

    file = path + '\\' + place + '.xls'
    wb = xlrd.open_workbook(filename=file)  # 打开文件
    sheet1 = wb.sheet_by_name('相对湿度')  # 通过名字获取表格

    shuju = sheet1.col_values(0)  # 用shuju获取第0列的全部包含空行的数据
    del shuju[0]
    times = []  # 存储非空数据
    i=0
    while i<len(shuju):
        zhi=shuju[i]
        times.append(zhi[0:10])
        i=i+24
    shuju2 = sheet1.col_values(2)
    del shuju2[0]
    hps = []  # 用hps存储 “日最高气压”
    for hp in shuju2:
        if len(str(hp)) > 0:
            hps.append(hp)
    # 创建一个字典（xuhao）让每一个日期都和一个序号关联起来，且该序号与日最高气压的序号一一对应
    xuhao = {}
    i = 0
    for time in times:
        xuhao[time] = i
        i = i + 1
    #选择一个月份
    month_0 = month#假设月份为2009/10
    #那么这个月的第一天表示为
    data_1 = str(month) + '/1 '
    #第一天对应的索引为
    num = xuhao[data_1]
    #2009到2010年每个月份对应的总天数
    yue = {}
    yue['2009/01'] = 31
    yue['2009/02'] = 28
    yue['2009/03'] = 31
    yue['2009/04'] = 30
    yue['2009/05'] = 31
    yue['2009/06'] = 30
    yue['2009/07'] = 31
    yue['2009/08'] = 31
    yue['2009/09'] = 30
    yue['2009/10'] = 31
    yue['2009/11'] = 30
    yue['2009/12'] = 31
    yue['2010/01'] = 31
    yue['2010/02'] = 28
    yue['2010/03'] = 31
    yue['2010/04'] = 30
    yue['2010/05'] = 31
    yue['2010/06'] = 30
    yue['2010/07'] = 31
    yue['2010/08'] = 31
    yue['2010/09'] = 30
    yue['2010/10'] = 31
    yue['2010/11'] = 30
    yue['2010/12'] = 31
    the_times = times[num:num+yue[month]]
    the_hp = hps[num:num+yue[month]]
    if contrast:
        if t:
            return the_times
        return the_hp
    plt.figure(figsize=(8,4))
    plt.plot(the_times,the_hp,"b--",linewidth=1)
    plt.xlabel("Time")
    plt.ylabel('Relative humidity (%)')
    plt.title(month + '月  日相对湿度变化情况')
    plt.xticks(rotation=-90)
    plt.rcParams['font.sans-serif']=['SimHei']

    fig, (ax0, ax1) = plt.subplots(nrows=2, figsize=(9, 6))
    ax0.hist(the_hp, 30, density=1, histtype='bar', facecolor='yellowgreen', alpha=0.75)
    ax0.set_title(month + '月  日相对湿度 概率分布直方图')
    ax1.hist(the_hp, 30, density=1, histtype='bar', facecolor='pink', alpha=0.75, cumulative=True, rwidth=0.8)
    ax1.set_title(month + '月  日相对湿度 累计概率分布')
    plt.rcParams['font.sans-serif'] = ['SimHei']

    plt.show()


def water_vapor(path=r'C:\Users\Ted\Desktop\地面观测数据',place='徐州', date='2009/02/30'):
    """画出data日的本站水汽压随时间变化的折线图"""

    file = path + '\\' + place + '.xls'
    wb = xlrd.open_workbook(filename=file)
    sheet1 = wb.sheet_by_name('水汽压')
    times = sheet1.col_values(0)
    del times[0]
    i=0
    xuhao={}
    for key in times:
        xuhao[key] = i
        i = i+1
    date_0 = date + ' 00时'
    start = xuhao[date_0]
    the_times = times[start:start + 24]
    station_pressures = sheet1.col_values(1)
    del station_pressures[0]
    the_sp0 = station_pressures[start:start + 24]
    plt.figure(figsize=(8,4))  # 创建绘图对象
    plt.plot(the_times,the_sp0,"b--",linewidth=1)  # 在当前绘图对象绘图，蓝色虚线，宽线度
    plt.xlabel("Time")
    plt.ylabel("水汽压（hPa）")
    plt.title(date + "日水汽压变化情况")
    plt.xticks(rotation=-90)
    plt.rcParams['font.sans-serif']=['SimHei']
    plt.show()


def shiqiu(path=r'C:\Users\Ted\Desktop\地面观测数据',place='徐州',date='2009/01/1'):
    """画出data日的本站湿球温度随时间变化的折线图"""

    file = path + '\\' + place + '.xls'
    wb = xlrd.open_workbook(filename=file)
    sheet1 = wb.sheet_by_name('湿球温度')
    times = sheet1.col_values(2)
    del times[0]
    i = 0
    xuhao={}
    for key in times:
        xuhao[key] = i
        i = i+1
    date_0 = date + ' 00时'
    start = xuhao[date_0]
    the_times = times[start:start + 24]
    station_pressures = sheet1.col_values(3)
    del station_pressures[0]
    the_sp0 = station_pressures[start:start + 24]
    plt.figure(figsize=(8,4))
    plt.plot(the_times,the_sp0,"b--",linewidth=1)
    plt.xlabel("Time")
    plt.ylabel("露点温度（℃）")
    plt.title(date +"日露点温度变化情况")
    plt.xticks(rotation=-90)
    plt.rcParams['font.sans-serif']=['SimHei']
    plt.rcParams['axes.unicode_minus'] = False  # 正确显示坐标轴负号
    plt.show()


def wind_velocity(path=r'C:\Users\Ted\Desktop\地面观测数据',place='徐州',date='2009/05/20'):
    """画出data日的本站2分钟平均风速和10分钟平均风速随时间变化的折线图"""

    file = path + '\\' + place + '.xls'
    wb = xlrd.open_workbook(filename=file)#打开文件
    sheet1 = wb.sheet_by_name('风')
    times = sheet1.col_values(0)
    del times[0]
    i=0
    xuhao={}
    for key in times:
        xuhao[key] = i
        i = i+1
    date_0 = date + ' 00时'
    start = xuhao[date_0]
    the_times = times[start:start+24]
    station_pressures = sheet1.col_values(2)
    del station_pressures[0]
    the_sp0 = station_pressures[start:start+24]
    station_pressures = sheet1.col_values(5)
    del station_pressures[0]
    the_sp1 = station_pressures[start:start+24]
    fig, ax = plt.subplots()
    ax.plot(the_times, the_sp0, label='2分钟平均风速')
    ax.plot(the_times, the_sp1, label='10分钟平均风速')
    ax.set(ylabel='wind velocity（m/s）', xlabel='Time', title='风速')
    ax.legend()
    plt.xticks(rotation=-90)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.show()

