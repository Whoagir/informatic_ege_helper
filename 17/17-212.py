data = [int(x) for x in open('17-4.txt')]

average = sum(data) / len(data)

count, mi = 0, 10**10
for i, n in enumerate(data):
   if i > 0:
     if (data[i-1] > average or data[i] > average) and \
        (data[i-1] + data[i]) % 10 == 9:
        mi = min( mi, data[i-1] + data[i] )
        count += 1

print( count, mi )
