# Автор: А. Богданов

k = [0]*8
for i in range(2**14):
  b = bin(i)
  if '11' not in b:
    k[b.count('1')] += 1

ans = sum( 4*3*3**(14-i)*k[i] for i in range(8) )

print(ans)