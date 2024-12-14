with open("26-155.txt") as F:
  N = int(F.readline())
  data = {}
  for _ in range(N):
    mark, s, cls = map( int, F.readline().split() )
    mark = 10000*cls + mark
    data[mark] = data.get(mark, 0) + s

data = sorted( data.items(), key = lambda x: (-x[1], -x[0]) )

print( data[0][0] % 10000, data[0][1] )


#-------------------------------------------
# Авторы: В. Ланская, Р. Ягафаров

f = open("26-155.txt")
n = int(f.readline())
data = [[[], [], [], []] for i in range (9999 + 1)]
for i in range (n):
    number, value, level = map(int, f.readline().split())
    data[number][level].append(value)
ans = []
for i in range (1000, 9999 + 1):
    for j in range (1, 4):
        ans.append([sum(data[i][j]), j, i])

ans.sort(reverse = True, key = lambda x : (x[0], x[-1], x[1]))

print(ans[0], ans[1])
print(ans[0][-1], ans[0][0])
