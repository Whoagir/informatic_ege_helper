F = open('26-2.txt', 'r')
k, n = map(int, F.readline().split())
a = []
room = [-1] * n
for i in range(n):
    x, y = F.readline().split()
    a.append((int(x), int(y)))
a.sort()
cnt = 0
for i in range(n):
    for j in range(n):
        if a[i][0] > room[j]:
            room[j] = a[i][1]
            break
line = (room.index(-1) - 1) // k
for i in range(n):
    if a[-1][0] < room[i]:
        cnt += 1
#print(room)
print(line + 1, cnt)
        
