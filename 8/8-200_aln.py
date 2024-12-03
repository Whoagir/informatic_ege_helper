#8.200_ALN Автор А.Л.Наймушин

def OK(n):
  a = n//100
  b = n//10%10
  c = n%10
  if a <=b and b <=c:
      return 1
  else: return 0

k=0
for i in range(111,1000):
     if OK(i):
          k+=1
print(k) # Rez 165
