f=open('17-1.txt')
a=[int(x) for x in f]
av=sum(a)/len(a)
c=0
sm=[]
for i in range(len(a)-2):
    if (a[i]<av or a[i+1]<av or a[i+2]<av) and (a[i]%7==0 and a[i+1]%7==0 or a[i]%7==0 and a[i+2]%7==0 or a[i+1]%7==0 and a[i+2]%7==0):
        c+=1
        sm.append(a[i]+a[i+1]+a[i+2])
print(c, max(sm))