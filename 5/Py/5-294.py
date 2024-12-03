# Автор: А. Сандарян

for N in range (1000,10000):
  s = sorted(x for x in str(N))
  if N % 2 == 0:
    R = int (s [3]+s [2]+s [1]+s [0]) // 2
  else:
    R = int(s[0]+s[1]+s[2]+s[3])*2
  if R == N + 1:
    print(R)
    break