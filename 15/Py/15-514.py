def D(x,d): return x % d == 0
def nD(x,d): return x % d != 0

def f(x, A):
  return D(x, 12) and (70 <= x <= 80) and nD(x, A)

count = 0
for A in range(1,100):
  if all( not f(x,A) for x in range(1,1000) ):
    print( A )
    count += 1

print( 'Ответ', count )


# Автор: А. Наймушин

for A in range (1,10000):
    flag = 1
    for x in range (1,100):
        f= (x % 12 == 0) and (x >=70 and x <= 80) and  (x % A != 0)
        if f:
            flag = 0
    if flag:
        print (A)
'''
1
2
3
4
6
8
9
12
18
24
36
72

'''
