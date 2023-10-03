from bs4 import BeautifulSoup
import requests
import os
import time

time_start = time.time() #開始計時

print("star...")

a=50

for i in range(2,a+1):
    url=(f"	https://eclass2.nttu.edu.tw/sysdata/doc/d/de1875eb4363a5c5/images/{i}.jpg")
    pic=requests.get(url)
    catch=str(i)+".jpg"
    catch = pic.content

    if not os.path.exists("Desktop/DSS/DSS_決策偏誤/"):
        os.mkdir("Desktop/DSS/DSS_決策偏誤/")

    with open("Desktop/DSS/DSS_決策偏誤/"+"img"+str(i-1)+".jpg","wb") as f:
        f.write(catch)

time_end = time.time()    #結束計時

time_c= time_end - time_start   #執行所花時間

print('Download completed!\n','total time cost:', time_c, 's')