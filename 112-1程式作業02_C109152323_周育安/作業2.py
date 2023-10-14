# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 14:22:34 2023

@author: YuAnChou
"""
import socket
from statistics import mean
from statistics import median
from statistics import pvariance
from statistics import pstdev
#-----------------------------------------------------------#
host_name=socket.gethostname()
ip_address=socket.gethostbyname(host_name)
#-----------------------------------------------------------#
num=[]
#-----------------------------------------------------------#
while(1):
    number=input("Enter number :")
    if(float(number)<0):
        sorted(num)
        break
    else:
        num.append(float(number))
print("---------------------------------------------")
print("Averange :{}".format(mean(num)),end=' ')
print("中位數：{}".format(median(num)),end=' ')
print("變異數：{}".format(pvariance(num)),end=' ')
print("標準差：{}".format(pstdev(num)))
print("---------------------------------------------")
print("IP Address :{}".format(ip_address))