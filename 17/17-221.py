data = [int(x) for x in open('17-1.txt')]

average = sum(data) / len(data)

def divs( x ):
    return  x % 3 == 0 and x % 5 != 0 and x% 11 != 0 and \
            x % 19 != 0

count, ma = 0, 0
for i, n in enumerate(data):
   if i > 0:
     if (data[i-1] < average or data[i] < average) and \
        (divs(data[i-1]) or divs(data[i])):
        ma = max( ma, data[i-1] + data[i] )
        count += 1

print( count, ma )
