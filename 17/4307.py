f=open('17-3.txt')
a=[int (x) for x in f]
ans=0
ans1=[]
for i in range(len(a)-2):
    if a[i]>a[i+1]>a[i+2]:
        ans+=1
    b=a[i]-a[i+2]
    ans1.append(b)
print(ans,min(ans1))