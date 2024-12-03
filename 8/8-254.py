count = 0
for i in range(int('10000',16), int('100000',16)):
  s = f"{i:X}"  
  if s[0] == 'F' and s[-1] == 'A' and s.count('3B') == 1:
    count += 1

print( count )

