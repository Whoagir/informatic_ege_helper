def f(a, n):
    return sum(a[::-1][i]*n**i for i in range(len(a)))

from string import digits, ascii_uppercase
let = digits + ascii_uppercase

for p in range(let.index('L')+1,37):
  for q in range(let.index('V')+1,37):
    for x in range(p):
        n = f( [let.index(x) for x in 'ALE'] + [x], p ) + \
            f( [let.index(x) for x in 'DANOV'], q )
        if n % 2023 == 0:
          print( p, q, x, n // 2023 )