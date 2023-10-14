# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 13:31:28 2023

@author: YuAnChou
"""
import socket
import datetime

def tier1(m,t1):
    return t1*1.63
def tier2(m,t2):
    if(m=='s'):
        return t2*2.38
    else:
        return t2*2.10
def tier3(m,t3):
    if(m=='s'):
        return t3*3.52
    else:
        return t3*2.89
def tier4(m,t4):
    if(m=='s'):
        return t4*4.80
    else:
        return t4*3.94
def tier5(m,t5):
    if(m=='s'):
        return t5*5.66
    else :
        return t5*4.60
def tier6(m,t6):
    if(m=='s'):
        return t6*6.41
    else:
        return t6*5.03

x=int(input("輸入月份："))
y=int(input("輸入用電數："))
z=int(input("輸入預算："))

if(x>5 and x<10):
    m='s'
else:
    m='w'
 
    
if(y<120):
    money=tier1(m,y)
    price=1.63
elif( y>120 and y<=330) :
    money=tier1(m,120)+tier2(m,y-120)
    if(m=='s'):
        price=2.38
    else:
        price=2.10
elif(y>330 and y<=500):
    money=tier1(m,120)+tier2(m,210)+tier3(m,y-330)
    if(m=='s'):
        price=3.52
    else:
        price=2.89
elif(y>500 and y<=700):
    money=tier1(m,120)+tier2(m,210)+tier3(m,170)+tier4(m,y-500)
    if(m=='s'):
        price=4.80
    else:
        price=2.94
elif(y>700 and y<=1000):
    money=tier1(m,120)+tier2(m,210)+tier3(m,170)+tier4(m,200)+tier5(m,y-700)
    if(m=='s'):
        price=5.66
    else:
        price=4.60
elif(y>1000):
    money=tier1(m,120)+tier2(m,210)+tier3(m,170)+tier4(m,200)+tier5(m,300)+tier6(m,y-1000)
    if(m=='s'):
        price=6.41
    else:
        price=5.03

print("電費：{}元\t可用電量：{}度".format(money,(z-money)/price))
print("-----------------------------------")
host_name=socket.gethostname()
ip_address=socket.gethostbyname(host_name)
print(f"IP Adderss : {ip_address}")
now_time=datetime.datetime.now()
print(f"現在時間 : {now_time}")
print("-----------------------------------")    
    