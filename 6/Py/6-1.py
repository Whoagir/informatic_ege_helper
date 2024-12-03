count = 0
for x in range(1,6):
  for y in range(1,6):
    if y < -x/3**0.5+6 and y > x/3**0.5:
       count += 1
print( count )

