data = [int(x) for x in open('17-1.txt')]

average = sum(data) / len(data)

count, ma = 0, 0
for i, n in enumerate(data):
   if i > 0:
     if (data[i-1] > average or data[i] > average) and \
        (data[i-1] % 17 == 0 or data[i] % 17 == 0):
        ma = max( ma, data[i-1] + data[i] )
        count += 1

print( count, ma )
