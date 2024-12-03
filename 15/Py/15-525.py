k = 10
def P(x): return 13*k <= x <= 19*k
def nP(x): return not P(x)
def Q(x): return 17*k <= x <= 23*k
def nQ(x): return not Q(x)
def fA(x): return a <= x <= b

def f(x):
  return (not(nP(x) <= Q(x))) <= (fA(x) <= (nQ(x) <= P(x)))

maxA = 0
for a in range(12*k, 25*k):
  for b in range(a+1, 25*k):
    if all( f(x) for x in range(12*k, 25*k) ):
      if b - a > maxA:
        maxA = b - a
        print( maxA/k, a/k, b/k )

