Rmin = 10**10
for N in range(1, 1000):
  s0 = f"{N:b}"
  s = s0 + str(N % 2)
  s += str(s0.count('1')%2)
  R = int(s, 2)
  if R > 2023 and R < Rmin:
    print( N, R )
    Rmin = R
