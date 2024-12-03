count = 0
for x in range(1,10):
  for y in range(1,10):
    if y < -x/3**0.5+10 and y > x/3**0.5:
       count += 1
print( count )

points = [ (x,y) for x in range(1,10) for y in range(1,10)
                 if y < -x/3**0.5+10 and y > x/3**0.5 ]
print( len(points) )

print( len( [ (x,y) for x in range(1,10) for y in range(1,10)
                 if y < -x/3**0.5+10 and y > x/3**0.5 ] ) )

