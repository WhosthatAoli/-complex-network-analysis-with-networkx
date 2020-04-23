# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import csv


# 执行函数
def work(browser,url):

    browser.get(url)
    ele_nums = []
    time.sleep(3)
    js = 'window.scrollTo(0, document.body.scrollHeight);'
    browser.execute_script(js)
    time.sleep(3)
    browser.execute_script(js)

    try:
        for link in browser.find_elements_by_xpath("//*[@data-artnum]"):
            if isContainClass(link.get_attribute('className'),'icon-pdf'):
                ele_num = link.get_attribute('data-artnum')
                ele_nums.append(ele_num)

        return ele_nums

    except:
        print("failure")


#用于判断某元素是否具有某class
def isContainClass(allClass,targetClass):
    #解析allClass,判断是否包含targetClass
    classArr = allClass.split(' ')
    result = False
    for str in classArr:
        if str == targetClass:
            result = True
            break
    return result




if __name__ == '__main__':

    url = 'https://ieeexplore.ieee.org/search/searchresult.jsp?queryText=communications&highlight=true&returnType=SEARCH&refinements=ContentType:Magazines&returnFacets=ALL&ranges=2017_2017_Year'
    baseUrl = 'http://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber='
    maxPageNumber = 3
    browser = webdriver.Chrome()
    allnumber = []

    if maxPageNumber <= 1:
        eleNums = work(browser,url)
        eleNums = list(set(eleNums))


    else:
        for i in range(1,66):
            url0 = url+'&pageNumber='+str(i)
            eleNums = work(browser,url0)
            eleNums = list(set(eleNums))
            print(eleNums)
            allnumber.append((eleNums))

    print(allnumber)
    with open('d:/2017.csv', 'w', encoding='gb18030') as f:
        f = csv.writer(f)
        f.writerows(allnumber)

