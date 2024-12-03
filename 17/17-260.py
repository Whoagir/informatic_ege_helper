# Автор: А. Кабанов

f = open('17-257.txt')
a = [int(x) for x in f]
mn4 = min(x for x in a if x%10==4)
mx4 = max(x for x in a if x%10==4)
ans = []
for i in range(len(a)-1):
    if a[i] + a[i+1] < mn4 + mx4:
        ans.append(a[i]+a[i+1])
print(len(ans), max(ans))

