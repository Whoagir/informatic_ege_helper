# Автор: А. Кабанов

f = open('17-257.txt')
a = [int(x) for x in f]
mx = max(x for x in a if x%2!=0)
ans = []
for i in range(len(a)-1):
    if 2 * (a[i] + a[i+1]) > mx:
        ans.append(a[i]+a[i+1])
print(len(ans), min(ans))
