count = 0
for x in range(1,15):
  for y in range(1,15):
    if y < -x/3**0.5+15 and y > x/3**0.5:
       count += 1
print( count )

