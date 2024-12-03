def alg(x):
  s = f"{x:b}"
  if x % 2 == 0:
    s = s + f"{s.count('1'):b}"
  else:
    s = '1' + s + '00'
  return int( s, 2 )

N = 1
count = 0
while N < 1000:
  if 500 <= alg(N) <= 700:
    print(N)
    count += 1
    # break
  N += 1

print( 'Всего: ', count )
