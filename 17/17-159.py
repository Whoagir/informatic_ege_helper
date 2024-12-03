a = [int(x) for x in open('17-3.txt')]

maxSum = -20000
count = 0
for i in range(1, len(a)):
  s = a[i] + a[i-1]
  if s % 3 == 0 and s % 6 != 0 and \
     abs(a[i]*a[i-1]) % 10 == 8:
     count += 1
     maxSum = max(maxSum, s)

print( count, maxSum )
