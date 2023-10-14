import time
import socket

n=int(input("Enter a number："))
ans=[1,1]
start=time.time()
for i in range(1,n):
    ans.append(ans[i-1]+ans[i])
end=time.time()
#print(ans)
print("----------------------------------------------")
print("Run Time：{} s".format(end-start))
print("IP Address：{}".format(socket.gethostbyname(socket.gethostname())))
print("----------------------------------------------")