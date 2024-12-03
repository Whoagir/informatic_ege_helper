import statistics
f = open('17-294.txt')
a = []
for s in f:
  a.append(int(s))

sum1 = 0
sum2 = 0
c = 0
max = 0
for i in range(len(a)-1):
  x1 = a[ i]
  x2 = a[i+1]
  while x1 > 0:
    sum1 = x1 % 10 + sum1
    x1 = x1 // 10
  while x2 > 0:
    sum2 = x2 % 10 + sum2
    x2 = x2 // 10
  if (((sum1 + sum2) ** 0.5) % 1 == 0) and ((a[ i] + a[i+1]) > statistics.mean(a)):
    c += 1
    if (sum1 + sum2) > max:
       max = sum1 + sum2
  sum1 = 0
  sum2 = 0
print(c, max)