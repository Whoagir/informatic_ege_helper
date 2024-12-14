# Автор: Д. Козлов

f = open('26-125.txt', 'r')
D, P = list(map(int, f.readline().split()))
dwarfs = []
for _ in range(D):
  dwarfs.append(list(map(int,f.readline().split())))
f.close()

dwarfs.sort()
pots = [0] * P
busy = [0] * P
cnt, max_cnt = 0, 0

for i in range(D):
    amount = dwarfs[i][1] // 2
    if amount >= 1:
        for j in range(P):
            if busy[j] == 0: extra = 0
            else: extra = 2
            if dwarfs[i][0] >= pots[j] and dwarfs[i][0] + extra <= 1440:
                if (1440 - (dwarfs[i][0] + extra)) >= amount:
                    pots[j] = dwarfs[i][0] + extra + amount
                    cnt += amount
                    max_cnt = max(max_cnt, amount)
                    busy[j] = 1
                else:
                    pots[j] = 1440
                    cnt += 1440 - (dwarfs[i][0] + extra)
                    max_cnt = max(max_cnt, 1440 - (dwarfs[i][0] + extra))
                    busy[j] = 1
                #print( j, tuple(dwarfs[i]), amount, pots )
                break
print(cnt,max_cnt)
# 27994 245