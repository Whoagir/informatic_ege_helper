f=open('17-390.txt')
a=[int(x) for x in f]
avr=[]
avrr=0
ans=[]
c=0
for i in range(len(a)):
    if str(a[i])[-2:]=='28':
        avr.append(a[i])
ar=sum(avr)/len(avr)
for i in range(len(a)-2):
    if (str(a[i])[-2:]=='11' and str(a[i+1])[-2:]=='11' and str(a[i+2])[-2:]!='11') or (str(a[i])[-2:]=='11' and str(a[i+2])[-2:]=='11' and str(a[i+1])[-2:]!='11') or (str(a[i+1])[-2:]=='11' and str(a[i+2])[-2:]=='11' and str(a[i])[-2:]!='11'):
        if len(str(a[i]))==4 or len(str(a[i+1]))==4 or len(str(a[i+2]))==4:
            if a[i]>ar and a[i+1]>ar and a[i+2]>ar:
                c+=1
                ans.append(a[i]+a[i+1]+a[i+2])
print(c,min(ans))