with open('17-3.txt') as f:
    a = [int(x) for x in f.readlines()]

count = 0
mx = 10**10
for i in range(2, len(a)):
  if a[i-2] < a[i-1] < a[i]:
    count += 1
    mx = min( mx, a[i] - a[i-2] )

print( count, mx )


