f=open('17-1.txt')
a=[int(x) for x in f]
# print(a)
av=sum(a)
ln=len(a)
avr=av/ln
ans=[]
c=0
for i in range(len(a)-1):
    if  (a[i]>avr or a[i+1]>avr) and (a[i]%17==0 or a[i+1]%17==0):
        ans.append(a[i]+a[i+1])
        c+=1
print(max(ans),c)