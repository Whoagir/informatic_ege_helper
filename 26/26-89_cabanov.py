# Автор: А. Кабанов

f = open( '26-89.txt' )
n = int(f.readline())
a = [int(f.readline()) for i in range(n)]
a = sorted(set(a), reverse=1)
gift = [a[0]]
for i in range(1,len(a)):
  if gift[-1] - a[i] >= 3:
    gift.append(a[i])

print( len(gift), gift[-1] )
