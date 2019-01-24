#自定义x轴刻度为时间样式

%matplotlib inline

import matplotlib.pyplot as plt
import numpy as np
import datetime
from matplotlib.dates import DayLocator, DateFormatter

x = [datetime.date.today() + datetime.timedelta(i) for i in range(30)]
y = np.sin(np.arange(30))
plt.figure(figsize=(12,6))
plt.plot(x, y)
# 设置X轴的时间间隔，MinuteLocator、HourLocator、DayLocator、WeekdayLocator、MonthLocator、YearLocator
plt.gca().xaxis.set_major_locator(DayLocator(interval=3))
# 设置X轴的时间显示格式
plt.gca().xaxis.set_major_formatter(DateFormatter('%y/%m/%d'))
# 自动旋转X轴的刻度，适应坐标轴
plt.gcf().autofmt_xdate()
plt.show()