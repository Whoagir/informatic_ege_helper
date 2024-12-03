count = 0
for i in range(int('10000',8), int('100000',8), 2):
  s = f"{i:o}"
  if s[0] == '7' and s.count('56') + s.count('65') == 1:
    count += 1

print( count )

