data = [int(x) for x in open('1.txt')]
n = len(data)
mn3 = min(x for x in data if x % 3 == 0)
mx3 = max(x for x in data if x % 10 == 3)
cnt = 0
mn = float('inf')
for i in range(n-1):
    if (mn3 <= data[i] <= mx3) + (mn3 <= data[i+1] <= mx3) == 1:
        cnt += 1
        mn = min(mn, data[i]**2+data[i+1]**2)
print(cnt, mn)
