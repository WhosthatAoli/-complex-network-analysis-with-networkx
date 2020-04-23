s = input("input a string:")
ls = s.split(" ")                            #分割字符串
print(len(ls))


import csv
with open('d:/degree.csv', 'w', encoding='gb18030') as f:
    f = csv.writer(f)
    f.writerows(allnumber)


d_order=sorted(central.items(),key=lambda x:x[1],reverse=True)            #字典排序 False从小到大 Ture从大到小

#二维数组转一维
a = [(4,2,3), (5, 9, 1), (7,8,9)]
from itertools import chain
list(chain.from_iterable(a))
