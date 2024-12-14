# Автор: Д. Статный

f = open('26-107.txt')
l, n = map(int, f.readline().split())
a = [list(map(int, f.readline().split())) for _ in range(n)]
a.sort(key = lambda x: (x[1], x[0]))
flights = [[a[0][0], a[0][1]]]
for x in a[1:]:
    if x[0] >= flights[-1][1]:
        flights.append([x[0], x[1]])
print(len(flights), flights[-1][0])
