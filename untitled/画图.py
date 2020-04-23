import pandas as pd
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np
from itertools import chain

with open('d:/degree1.csv','r') as file:
    data = pd.read_csv(file)
    print(data)
    train_data = np.array(data)  # np.array()
    train_x_list = train_data.tolist()  # list
    print(train_x_list)

a = list(chain.from_iterable(train_x_list))
print(a)

dict_cnt={}   #dict_cnt=dict()
for item in a:
   if item in dict_cnt:   #直接判断key在不在字典中
      dict_cnt[item]+=1/12251
   else:
      dict_cnt[item]=1/12251

print(dict_cnt)

x = list(dict_cnt.keys())
y = list(dict_cnt.values())
print(x)
print(y)
def func(x,a,b):
    return a/(x**b)

popt, pcov = curve_fit(func, x, y)
a=popt[0]                   #popt里面是拟合系数，读者可以自己help其用法
b=popt[1]
print(a,b)
yvals=func(x,a,b)
plot1=plt.plot(x, y, '*',label='original values')
plot2=plt.plot(x, yvals, 'r',label='curve_fit values')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.legend(loc=4)              #指定legend的位置,读者可以自己help它的用法
plt.title('curve_fit')
plt.show()

