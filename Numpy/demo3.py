import numpy as np

list = [1,4,9,16,25]
list1 = np.arange(1,11).reshape(2,-1)  #生成1 - 10按指定行数（列数缺省）
print(list1,'\n')

list2 = np.exp(list)
print(list2,'\n')

list3 = np.exp2(list)
print(list3,'\n')

list4 = np.sqrt(list)
print(list4,'\n')

list5 = np.sin(list)
pirnt(list5,'\n')

list6 = np.log(list)
pirnt(list)