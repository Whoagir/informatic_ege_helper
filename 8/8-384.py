
count = 0
for i in range(8**4, 8**5):
  s = f"{i:o}"
  if len(s) == len(set(s)) and \
     all((ord(s[k-1])+ord(s[k+1])) % 2 == 1 for k in [1,2,3]):
     count += 1

print( count )
