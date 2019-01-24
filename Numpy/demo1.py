

import numpy as np

l = [1,3,5,7,9]
list = np.array(l)
print(list)
print("行列：",list.shape)
print("个数：",list.size)
print("类型：" ,list.dtype)
print("维度：",list.ndim)
print("字节：",list.itemsize)