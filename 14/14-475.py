n = 3 * 289**2024 + 81 * 49**121 - 9 * 16**81 - 6011
B = 31
s = 0
while n:
  d = n % B
  s += d if d <= 17 else 0
  n //= B

print( s )