count = 0
for i in range(int('1000AB',16), int('1000000',16), 256):
  s = f"{i:X}"  
  if s[0] != '1' and s.endswith('AB'):
    count += 1

print( count )

