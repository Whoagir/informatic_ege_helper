def F(n):
  if n < 2: return 1
  if n % 3 == 0:
    return F(n//3) - 1
  else:
    return F(n-1) + 7

count = 0
a = []
for i in range(1, 100000):
  R = F(i)
  a.append(R)
  if R == 35:
    #print( i )
    count += 1

print( "Ответ:", count )

from collections import Counter
x = Counter(a)
print( x.most_common(3) )