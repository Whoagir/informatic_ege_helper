# Автор: К. Багдасарян

data = [int(x) for x in open('17-411.txt')]
n = len(data)
mx7 = max(x for x in data if x % 10 == 7)
cnt = 0
mx = -float('inf')
for i in range(n-1):
    if str(data[i])[0] == str(data[i+1])[0]:
        if (data[i] % 10 == 7 and 100 <= data[i] <= 999) or\
           (data[i+1] % 10 == 7 and 100 <= data[i+1] <= 999):
            if (data[i]+data[i+1]) < mx7:
                cnt += 1
                mx = max(mx, data[i]+data[i+1])
print(cnt, mx)
