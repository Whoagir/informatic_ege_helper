# Автор: М. Ишимов

f = open('26-95.txt')
n = int(f.readline())
a = [ [0] * 5001 for x in range(2001) ]
town, count = set(), set()
ans = []

for i in range(n):
    house, door = map(int, f.readline().split())
    a[house][door] += 1
    town.add(house)

for house in town:
    s = [0]
    for p in range(1, 5001):
        if a[house][p] == 0: s.append(0)
        elif a[house][p-1] == 0 or p == 1: s.append(1)
        else: s[-1] += 1
    door = 0
    for p in range(1, len(s) - 1):
        x,y,z = s[p-1], s[p], s[p+1]
        if y == 0:
            door += x + 1
            if x+z >= 3:
                ans.append( (house, door) )
                count.add(house)

numb = min([x[1] for x in ans if x[0] == max(ans)[0]])
print(len(count), numb)