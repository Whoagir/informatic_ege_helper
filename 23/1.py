d={1:1}
for i in range(2,57): #МАКСИМАЛЬНО ВОЗМОЖНОЕ
    d[i]=0
print(d)
for i in range(1,10): #НЕ СОДЕРЖИТ 10
    d[i+1]=d[i]+d[i+1]
    d[i*2]=d[i]+d[i*2]
d[10]=0
for i in range(11,26): #СОДЕРЖИТ 25
    d[i+1]=d[i]+d[i+1]
    d[i*2]=d[i]+d[i*2]
for i in range(26,57):#
    d[i]=0
for i in range(25,29):
    d[i+1]=d[i]+d[i+1]
    d[i*2]=d[i]+d[i*2]
print(d[28])