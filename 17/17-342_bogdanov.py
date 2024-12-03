# Автор: А. Богданов

a = [*map(int,open('17-342.txt'))]
mn = min(x for x in a if x%37==0)
mx = max(x for x in a if x%73==0)
if mn>mx: mn,mx = mx,mn
sm = 10000; k = 0
for x,y in zip(a,a[1:]):
  if (mn<x<mx) != (mn<y<mx):
    k += 1
    sm = min(sm,x+y)
#print(mn,mx)
print(k,sm)
