F = open('26-4.txt')
n = int(F.readline())
a = [0] * 60*24
for i in range(n):
    s, f = list(map(int, F.readline().split()))
    for j in range(s, f+1):
        a[j] += 1
mx = max(a)
k = 0
for i in range(1,1440):
    if a[i] == mx and a[i] > a[i-1]:
        k += 1
print(k, mx)

