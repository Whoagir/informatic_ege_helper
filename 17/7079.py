f=open('17-388.txt')
a=[int(x) for x in f]
a1=[x[0] for x in f]
v=a1.count('6')
sm=sum(a)
mx=max(a)
ans=0
ans1=[]
for i in range(len(a)-2):
    if sm>mx and v<=1:
        ans+=1
        b=a[i]+a[i+1]+a[i+2]
        ans1.append(b)
print(ans, min(ans1))