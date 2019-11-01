# coding:utf-8
from datetime import *
import time
import requests
from bs4 import BeautifulSoup
import re
import csv
import xlwt

nowticks = time.time()
print ("当前时间戳为:", nowticks)

biaoflag = nowticks
hang = 0
f = xlwt.Workbook()
sheet1 = f.add_sheet(u'shishi',cell_overwrite_ok = True)
while 1:
    # pastflag = (datetime.now() - timedelta(seconds=60)).strftime('%M')
    nowflag = time.time()

    if (nowflag - biaoflag >= 1200):
        print("20分钟到，执行一次")
        biaoflag = nowflag
        r = requests.get('https://zst.cjcp.com.cn/cjw11x5/view/11x5zonghe-2-gd11x5-11-3-50.html')
        
        demo = r.text

        soup = BeautifulSoup(demo, 'html.parser')
        #print(soup.prettify())

        ##获取开奖号码
        wm = soup.find_all("td",class_="WhiteBack RedFont")
        rm = r'<td class="WhiteBack RedFont">(.*?)</td>'
        wd = re.findall(rm, str(wm) ,re.S | re.M)
        #print(wd)#近50期开奖号码
        print(wd[-1])#最终要的最新一期开奖号码

        ##获取开奖期数
        date = soup.find_all("td",class_="z_bg_05")
        res_date = r'<td class="z_bg_05">(.*?)</td>'
        date_td = re.findall(res_date, str(date) ,re.S | re.M)

        my_list = []

        for i in range(len(date_td)):
            if i % 21 == 1:
                my_list.append(date_td[i])
        
        #print(my_list)  #近50期开奖期数
        print(my_list[-1]) #最终需要的最新一期开奖期数

       
       
        sheet1.write(hang,0,my_list[-1])
        sheet1.write(hang,1,wd[-1])


        k = ""
        s = []
        temp = []
        ooo = wd


        for i in range(len(ooo)):
            #print(win_td[i])
            k = wd[i]
            #print(k.split(" "))
            temp = k.split(" ")
            s = sorted(temp)
            #print(s)
            #print(type(s))
    
            b = 3
            for ii in range(len(s)):
                sheet1.write(hang, b, s[ii])
                b = b + 1
        
        f.save("timer.xls")
        hang = hang + 1

    else:
        pass





