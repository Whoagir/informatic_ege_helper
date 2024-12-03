data = [int(x) for x in open('17-1.txt')]

average = sum(data) / len(data)

count, ma = 0, 0
for i, n in enumerate(data):
   if i > 0:
     if (data[i-1] < average or data[i] < average) and \
        (abs(data[i-1]) % 100 == 13 or abs(data[i]) % 100 == 13):
        ma = max( ma, data[i-1] + data[i] )
        count += 1

print( count, ma )
