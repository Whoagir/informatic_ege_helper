count = 0
for x in range(1,9):
  for y in range(-4,5):
    if y > -x/3**0.5 and y < x/3**0.5:
       count += 1
  print( x, count )
print( count )

