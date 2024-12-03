# Автор: А. Кабанов

f = open('17-257.txt')
a = [int(x) for x in f]
m7 = min(x for x in a if x%7==0)
m13 = min(x for x in a if x%13==0)
if m7>m13:
    k = len([x for x in a if x%7==0])
    m = max(x for x in a if x%7==0)
else:
    k = len([x for x in a if x%13==0])
    m = max(x for x in a if x%13==0)
print(k,m)
