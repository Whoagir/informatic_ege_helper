def f(a, n):
    return sum(a[::-1][i]*n**i for i in range(len(a)))

for p in range(5,37):
  for q in range(6,37):
     if int('234',p) == int('345',q):
        print( int('234',p) )
