import socket
import matplotlib.pyplot as plt

letternum=[0]*26
letter=[chr(ord('A') + i) for i in range(26)]
text=[]
with open('snow-white.txt','r') as file:
    for i in file.readlines():
        text.append(i.strip())
for i in range(len(text)):
    for j in text[i]:
       if(ord(j.lower())>96 and ord(j.lower())<123):
           letternum[ord(j.lower())-97]=letternum[ord(j.lower())-97]+1
print(letternum)
print("-------------------------")
print("IP Address：{}".format(socket.gethostbyname(socket.gethostname())))
print("-------------------------")
plt.bar(letter,letternum)
plt.show()