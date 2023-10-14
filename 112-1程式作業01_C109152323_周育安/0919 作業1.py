import socket
import datetime

ans=[]

for a in range(0,101):
    for b in range(a+1,101):
        for c in range(b+1,101):
            for d in range(c+1,101):
                if(a**3+b**3+c**3==d**3):
                    ans.append([a,b,c,d])
for i in ans:
    print(i)
print("共有 %d 個組合" %(len(ans)))
print("-----------------------------------")
host_name=socket.gethostname()
ip_address=socket.gethostbyname(host_name)
print(f"IP Adderss : {ip_address}")
now_time=datetime.datetime.now()
print(f"現在時間 : {now_time}")
print("-----------------------------------")                    
    
