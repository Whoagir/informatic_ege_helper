# Автор: А. Кабанов

f = open('17-257.txt')
a = [int(x) for x in f]

mn = min(x for x in a if x%2!=0)
mx = max(x for x in a if x%2!=0)
ans = []
for i in range(len(a)-1):
    if (a[i]+a[i+1])%2==0 and a[i]+a[i+1] > mn + mx:
        ans.append(a[i]+a[i+1])
print(len(ans), min(ans))
