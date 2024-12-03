N = (7**(9**2-1) - (10-3)**4 + int('234',7)) * 5 * 8 // 6

N = abs(N)

count4 = 0
while N:
  if N % 7 == 4: count4 += 1
  N //= 7

print( count4 )