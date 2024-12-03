data = [int(x) for x in open('17-4.txt')]

average = sum(data) / len(data)

def divs( x ):
    return  x % 7 == 0 and x % 3 != 0 and x% 11 != 0 and \
            x % 13 != 0

count, mi = 0, 10**10
for i, n in enumerate(data):
   if i > 0:
     if (data[i-1] < average or data[i] < average) and \
        (divs(data[i-1]) or divs(data[i])):
        mi = min( mi, data[i-1] + data[i] )
        count += 1

print( count, mi )
