data = list( map(int, open('17-365.txt')) )

res = [ (a, b) for a, b in zip(data,data[1:])
               if (abs(a) % 10 == 1) ^ (abs(b) % 10 == 1) ]

max1 = max( (a+b)/2 for a, b in res )

res = [ (a, b) for a, b in res
               if a < max1 and b < max1 ]

minRes = min( min(a,b) for a, b in res )
maxRes = max( max(a,b) for a, b in res if minRes in (a,b) )

print( len(res), maxRes )

