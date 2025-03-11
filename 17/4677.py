f=open('17-1.txt')
a=[int(x) for x in f]
avr=sum(a)/len(a)
ans=[]
for i in range(len(a)-2):
    if a[i]<avr or a[i+1]<avr or a[i+2]<avr:
        if str(a[i]).count('8')>=1 or str(a[i+1]).count('8')>=1 or str(a[i+2]).count('8')>=1:
            ans.append(a[i]+a[i+1]+a[i+2])
print(len(ans), max(ans))