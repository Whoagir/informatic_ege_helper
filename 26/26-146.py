# Автор: И. Карпаченв

f = open('26-146.txt')
n = int(f.readline())
works = []
for i in range(n):
    t, c = map(int, f.readline().split())
    works.append((t, c))
f.close()

works.sort(key=lambda x: (x[0], -x[1]))
current_time = 0
count = 0
pack = []
for work in works:
    t, c = work
    if current_time < t:
        current_time += 1
        pack.append(c)
    else:
        min_profit = min(pack)
        index = pack.index(min_profit)
        if c > min_profit:
            pack[index] = c
print(sum(pack), min(pack))
