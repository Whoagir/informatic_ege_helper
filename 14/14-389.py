x15 = list(range(2,15))
for x in x15:
  s = int(f"3{x}15{x}", 15)
  b1 = int(f"3{x}51")
  s += 1*b1**2 + 2*b1 + 3
  s += x**x
  b2 = int(f"1{x}3")
  s += 1*b2**2 + x*b2 + 3
  s += int(f"1{x}2", x+1)
  if s % 13 == 0:
    print(x)
    break

res = ""
while s:
  res = "0123456789ABC"[s%13] + res
  s //= 13

print( res )

