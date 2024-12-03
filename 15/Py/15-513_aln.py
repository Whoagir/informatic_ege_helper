# Автор: А. Наймушин

def D(x,d): return x % d == 0
def nD(x,d): return x % d != 0

def f(x, A):
  return (160 <= x <= 180)<= (D(x, 35) <= D(x, A))

count = 0
for A in range(1,1000):
  if all(  f(x,A) for x in range(1,1000) ):
    print( A )
    count += 1

print( 'Ответ', count )

'''
1
5
7
25
35
175
Ответ 6
'''
