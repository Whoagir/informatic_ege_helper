from itertools import combinations

N = 10
N7 = 5
count = 0
for p in combinations(range(N), N-N7):
  w = ['7']*N
  for i in range(N-N7): w[p[i]] = '0'
  w = '.' + ''.join(w) + '.'
  if '77' in w: continue
  k = 1
  for i in range(1,N+1):
    if w[i] != '7':
      p = 7 if i > 1 else 6
      if '7' in [w[i-1], w[i+1]]: p -= 3
      # print(p)
      k *= p
  print( w, k )
  count += k

print( count )


# Автор: А. Богданов

k = 1*4*1*4*1*4*1*4*1*4 *5 + 3*1*4*1*4*1*4*1*4*1;
print( k )