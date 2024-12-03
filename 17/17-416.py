data = [int(x) for x in open('1.txt')]
n = len(data)
mx1 = max(x for x in data if x % 10 == 1)
cnt = 0
mn = float('inf')
for i in range(n-3):
    sm = data[i]+data[i+1]+data[i+2]+data[i+3]
    if sm % 2 != 0 and max(data[i],data[i+1],data[i+2],data[i+3]) < mx1:
        cnt += 1
        mn = min(mn, sm)
print(cnt, mn)

