import time
import socket
def fabo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fabo(n-1) + fabo(n-2)
n=int(input("Enter a number："))
ans=[]
start=time.time()
for i in range(1,n+1):
    ans.append(fabo(i))
end=time.time()
print(ans)
print("----------------------------------------------")
print("Run Time：{}".format(end-start))
print("IP Address：{} s".format(socket.gethostbyname(socket.gethostname())))
print("----------------------------------------------")