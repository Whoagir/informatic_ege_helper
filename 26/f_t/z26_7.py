F = open('26-7.txt', 'r')
k, n = map(int, F.readline().split())
a = []
for i in range(n):
    x, y = map(int, F.readline().split())
    a.append((x, y)) 


a.sort()
print(a[:20])
room = [-1] * k
mx = 0
for i in range(n):
    ind = 0
    for j in range(k):
        if room[j] <= room[ind]:
            ind = j
    if room[ind] < 24*60*7 and a[i][0] < 24*60*7 and a[i][1] > room[ind]:
        if room[ind] - a[i][0] > mx:
            mx = room[ind] - a[i][0]
        room[ind] = a[i][1] + 31
        last = ind
        
    
print(mx, last+1)

