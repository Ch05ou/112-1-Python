import random
import os
import socket
poker=[]
player1=[]
player2=[]
player3=[]
player4=[]
face=['黑桃','紅心','菱形','梅花']   
number=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
for i in face:
    for j in number:
        poker.append(i+j)
for i in range(0,52):
    cardnum=random.randint(0,len(poker)-1)
    if(i%4==0):
        player1.append(poker[cardnum])
        del poker[cardnum]
    elif(i%4==1):
        player2.append(poker[cardnum])
        del poker[cardnum]
    elif(i%4==2):
        player3.append(poker[cardnum])
        del poker[cardnum]
    else:
        player4.append(poker[cardnum])
        del poker[cardnum]

print("玩家1的牌：{}".format(player1))
print("玩家2的牌：{}".format(player2))
print("玩家3的牌：{}".format(player3))
print("玩家4的牌：{}".format(player4))
print("----------------------------------")
print("IP Address：{}".format(socket.gethostbyname(socket.gethostname())))
print("----------------------------------")

with open("ex12-C109152323-周育安.txt",'w') as file:
    file.write("玩家1：")
    for i in player1:
        file.write(i)
        file.write(" ")
    file.write("\n")
    file.write("玩家2：")
    for i in player2:
        file.write(i)
        file.write(" ")
    file.write("\n")
    file.write("玩家3：")
    for i in player3:
        file.write(i)
        file.write(" ")
    file.write("\n")
    file.write("玩家4：")
    for i in player4:
        file.write(i)
        file.write(" ")
    file.write("\n")

