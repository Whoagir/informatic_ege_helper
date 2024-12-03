a = [ int(s)
      for s in open("17-205.txt") ]

count = 0
ma = -20000;
for i in range(1,len(a)):
  if abs(a[i]-a[i-1]) % 74 == 0:
    count += 1
    ma = max( ma, a[i]+a[i-1] )

print( count, ma )