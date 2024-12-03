def count1(n):
    count = 0
    while n>0:
        if n % 2 == 1:
            count +=1
        n //= 2
    return count

def count0(n):
    count = 0
    while n>0:
        if n % 2 == 0:
            count += 1
        n //=2
    return count

f = open("1.txt")
a = []
m = 0
ms = 0
k = 0
for i in f:
    a.append(int(i))
for i in range(len(a)-2):
    if (count1(a[i]) >=3 and count1(a[i+1]) >=3 and count0(a[i])>0 and count0(a[i+1]) > 0) or (count1(a[i+1])>=3 and count1(a[i+2])>=3 and count0(a[i+1])>0 and count0(a[i+2]) > 0) or (count1(a[i])>=3 and count1(a[i+2]) >= 3 and count0(a[i])>0 and count0(a[i+2]) > 0):
        k += 1
        m = max(a[i],a[i+1],a[i+2])
        if m>ms:
            ms = m
    
print(k,ms)
