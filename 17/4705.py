f=open('17-257.txt')
a=[int(x) for x in f]
n=[]
v=10128
for i in  range (len(a)-1):
    if a[i]+a[i+1]<v:
        n.append(a[i]+a[i+1])
print(len(n), max(n))