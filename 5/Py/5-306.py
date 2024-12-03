def alg( n ):
  s = f"{n:b}"
  if len(s) % 2 == 0:
    s += '10'
  else:
    s = '11' + s
  return s

print( len([n for n in range(100, 201)
              if alg(n)[-1] == '0'  ]) )

