#自定义x轴刻度为数字样式

%matplotlib inline

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

x = np.arange(30)
y = np.sin(x)
plt.figure(figsize=(12,6))
plt.plot(x, y)
# 设置X轴的刻度间隔
plt.gca().xaxis.set_major_locator(MultipleLocator(3))
# 设置X轴的刻度显示格式
plt.gca().xaxis.set_major_formatter(FormatStrFormatter("%d-K"))
# 自动旋转X轴的刻度，适应坐标轴
plt.gcf().autofmt_xdate()
plt.show()