x = 8**888 + 15*15**1515 - 2**444
count = 0
for d in range(1,7):
 count += oct(x).count('7'+str(d))
print(count)

s = oct(x)
count = 0
for a, b in zip(s,s[1:]):
  if a == '7' and b not in ['7','0']:
    count += 1
print( count )    
  