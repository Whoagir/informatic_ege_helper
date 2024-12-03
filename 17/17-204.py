data = [int(x) for x in open('17-204.txt')]

def cond(x):
  return x > 0 and x % 10 == 9

ma = 0
count = 0
for i in range(2,len(data)):
  if (not cond(data[i-2])) and cond(data[i-1]) and \
     (not cond(data[i])):
    count += 1
    ma = max(ma, sum(data[i-2:i+1]))

print( count, ma)

