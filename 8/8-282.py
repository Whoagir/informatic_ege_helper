# 1-й способ
count = 0
for first in range(1,10):
  for last in range(0,10):
    len3 = len(str(last**3))
    count += 10**(7 - 3 - 1 - len3)

print( count )

# 2-й способ
def valid( s ):
  first = int(s[0])
  last = int(s[-1])
  return int(s[1:3]) == first**2 and \
         (last**3 in [int(s[-2]), int(s[-3:-1]), int(s[-4:-1])])

count = 0
for first in range(1,10):
  for x in range(0,10000):
    s = f"{first}{first**2:02d}{x:04d}"
    if valid(s):
       count += 1
       #print( s )
print( count )