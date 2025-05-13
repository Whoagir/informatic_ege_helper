f=open('17-336.txt')
a=[int(x) for x in f]
a1=sorted(a)[::-1]
ans=[]
mx=0
for i in range(len(a)):
    if a1[i]%37==0:
        mx=a1[i]
        break
for i1 in range(len(a)-1):
    if a[i1]%mx==0 or a[i1+1]%mx==0:
        if (a[i1]+a[i1+1])%mx>30:
            ans.append(a[i1]+a[i1+1])
print(len(ans), min(ans))