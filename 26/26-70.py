# Автор: А. Кабанов

f = open('26-70.txt')
n = int(f.readline())
a = [int(x) for x in f]
a.sort()

s = a[0]
new = []

for i in range(1,n):
    if a[i]-s>1:
        diff = a[i]-s-1
        new += [diff]
    s+=a[i]
print(new)
print(len(new),sum(new))
        
