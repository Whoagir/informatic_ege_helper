with open('17-3.txt') as f:
    a = [int(x) for x in f.readlines()]

count = 0
mx = -20000
for i in range(2, len(a)):
    P = a[i]*a[i-1]*a[i-2]
    S = a[i]+a[i-1]+a[i-2]
    if P % 7 == 0 and abs(S) % 10 == 5:
        count += 1
        mx = max(mx, S)
print(count, mx)


