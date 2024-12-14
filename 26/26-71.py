# Автор: А. Кабанов

f = open('26-71.txt')
N, S = map(int, f.readline().split())
d = {}
for i in range(N):
    code, w = map(int,f.readline().split())
    d[code] = d[code]+[w] if code in d else [w]

count = 0
max_ost = 0
max_code = 0
for code in sorted(d):
    a = d[code]
    a.sort()
    s = 0
    while len(a)>0 and s+a[0]<=500:
        s+=a[0]
        a.pop(0)
    count+=len(a)
    if sum(a)>max_ost:
        max_ost = sum(a)
        max_code = code

print(count, max_code)



