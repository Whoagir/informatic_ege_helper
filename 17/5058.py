f=open('17-282.txt')
a=[int(x) for x in f]
a1=min([a[n] for n in range(len(a)) if a[n]%37==0])
sma=10
ans=[]
for i in range(len(a)-1):
    if sum(map(int,str(a[i])))==sma or sum(map(int,str(a[i+1])))==sma:
        ans.append(a[i]+a[i+1])
print(min(ans), len(ans))