# Автор: А. Кабанов

a = [int(x) for x in open( '17-338.txt' )]
m = min(a)
ans = []
for i in range(len(a)-1):
  if a[i]%117 == m or a[i+1] % 117 == m:
    ans.append( a[i]+a[i+1] )
print( len(ans),max(ans) )