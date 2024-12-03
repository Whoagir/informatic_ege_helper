# Автор: А. Кабанов

f = open('17-257.txt')
a = [int(x) for x in f]

k11 = len([x for x in a if x%11==0])
k17 = len([x for x in a if x%17==0])
if k11>k17:
    m = min(x for x in a if x%11==0)
    print(k11, m)
else:
    m = max(x for x in a if x%17==0)
    print(k17,m)
