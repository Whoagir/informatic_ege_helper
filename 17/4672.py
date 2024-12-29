f=open('17-1.txt')
a=[int (x) for x in f]
av=sum(a)
ln=len(a)
avr=av/ln
ans=[]
c=0
for i in range(len(a)-2):
    if a[i]>avr or a[i+1]>avr or a[i+2]>avr:
        ans.append(a[i]+a[i+1]+a[i+2])
        c+=1
print(c,max(ans))