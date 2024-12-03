data = [int(x) for x in open('17-4.txt')]

average = sum(data) / len(data)

def valid( x ):
    return '7' in str(x)

count, mi = 0, 10**10
for i, n in enumerate(data):
   if i > 0:
     if (data[i-1] < average or data[i] < average) and \
        (valid(data[i-1]) or valid(data[i])):
        mi = min( mi, data[i-1] + data[i] )
        count += 1

print( count, mi )
