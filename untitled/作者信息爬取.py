import requests
import  csv
from bs4 import BeautifulSoup
import re
import pandas as pd
import numpy as np


user_agent= 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 \
             (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
headers = {'User-Agent':user_agent}

allwritername = []
alltitle = []

with open('d:/wirelessmagazine2017-2020.csv','r') as file:
    data = pd.read_csv(file)
    print(data)
    train_data = np.array(data)  # np.ndarray()
    train_x_list = train_data.tolist()  # list
    print(train_x_list)                                          #dataframe转list

    for i in train_x_list:                                       #为二维数组
        try:
            for j in i:
                if j == j:
                    writers = requests.get('https://ieeexplore.ieee.org/document/{}'.format(j))
                    writers.encoding = 'utf-8'

                    p = BeautifulSoup(writers.text,'lxml')
                    title = p.title.string                                          #标题
                    print(title)
                    alltitle.append(title)
                    #print(writers.text)
                    str = writers.text
                    #print(str)
                    record1 = re.findall(r"authors(.+?)issn",str)

                    record11 = ''.join(record1)
                    #print(record11)
                    record2 = re.findall(r'"name":"(.+?)","affiliation"',record11)
                    #print(record2)                 #作者
                    allwritername.append(record2)
        except:
            pass
        continue 
print(alltitle)
print(allwritername)
with open('d:/writerwirelessmagazine2017-2020.csv','w',encoding = 'gb18030') as f:
    f = csv.writer(f)
    for i in range(0,len(alltitle)):
        row = []
        row.append(alltitle[i])
        for x in range(0,len(allwritername[i])):
            row.append(allwritername[i][x])
        f.writerow(row)