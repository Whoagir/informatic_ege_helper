def F(n):
  if n == 0: return 1
  if n <= 10: return F(n-1)
  if n <= 100: return 2.2*F(n-3)
  return 1.7*F(n-2)

print(int(F(22)))

