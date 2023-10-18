import time
import socket

num1,num2=input("Enter a number :").split()
sum=0
ans=[]
start=time.time()
IPaddress=socket.gethostbyname(socket.gethostname())
for i in range(int(num1),int(num2)):
    if(i%4==0 or i%9==0):
        ans.append(i)
        sum=sum+i
end=time.time()
print(ans)
print("共有 {} 個".format(len(ans)))
print("總和：{}".format(sum))
print("------------------------------------------")
print("Run time :{} s".format(end-start))
print("IP Address：{}".format(IPaddress))
print("--------------------------------------------")