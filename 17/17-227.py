data = [int(x) for x in open('17-1.txt')]

average = sum(data) / len(data)

count, ma = 0, 0
for i, n in enumerate(data):
   if i > 1:
     if data[i-2] > average or data[i-1] > average or data[i] > average:
        ma = max( ma, data[i-2] + data[i-1] + data[i] )
        count += 1

print( count, ma )
