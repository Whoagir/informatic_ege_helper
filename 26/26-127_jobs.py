# Автор: Е. Джобс

with open('26-127.txt') as f:
    n = int(f.readline())
    s = [int(f.readline()) for _ in range(n)]

# список потребности в свободном месте в i минуту (от 1 до 1443)
# st[5] - сколько гномов хотят начать варить в 5 минут
st = [0]*1443
for x in s:
    st[x] += 1

# ищем максимальное количество желающих гномов во все 6 минут
# st[i] + st[i+1] + st[i+2] + st[i+3] + st[i+4] + st[i+5]
mn_p = max(sum(st[i:i+6]) for i in range(n))

print(mn_p)

s.sort() # n гномов

# komf - список,в котором запоминаем, кому было комфортно, кому нет
# 1 (комфортно), 0(некомфортно)
komf = [1]*n
# для каждой минуты сохраняем информацию о том, какие котлы заняты
# -1 - свободно
# х - индекс гнома, который занял котёл
tline = [[-1]*(mn_p+1) for _ in range(1450)]

for i, t in enumerate(s):
  # перебираем котлы
  for p in range(mn_p):
    # если котёл свободен
    if tline[t][p] == -1:
      # и свободны соседние места
      if tline[t][p-1] == tline[t][p+1] == -1:
        # выбираем и бронируем на 6 минут этот котёл
        for j in range(t, t+6):
          tline[j][p] = i
        break
  else:
    # перебираем котлы
    for p in range(mn_p):
      # если котёл свободен
      if tline[t][p] == -1:
        komf[i] = 0
        if tline[t][p-1] != -1:
          komf[ tline[t][p-1] ] = 0
        if tline[t][p+1] != -1:
          komf[ tline[t][p+1] ] = 0
        for j in range(t, t+6):
          tline[j][p] = i
        break

print(sum(komf))

