data = [int(x) for x in open('17-4.txt')]

average = sum(data) / len(data)

count, ma = 0, 0
for i, n in enumerate(data):
   if i > 0:
     if (data[i-1] < average and data[i] < average) and \
        (data[i-1] % 100 == 19 or data[i] % 100 == 19):
        ma = max( ma, data[i-1] + data[i] )
        count += 1

print( count, ma )
