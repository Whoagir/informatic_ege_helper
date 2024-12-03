# Автор: А. Кабанов

f = open('17-257.txt')
a = [int(x) for x in f]

m0 = max(x for x in a if x%2==0)
m1 = max(x for x in a if x%2==1)

if m0>m1:
    k = len([x for x in a if x%2==0])
    m = min(x for x in a if x%2==0)
else:
    k = len([x for x in a if x%2!=0])
    m = min(x for x in a if x%2!=0)
print(k,m)
