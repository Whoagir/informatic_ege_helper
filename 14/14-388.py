d8 = '01234567'
done = False
for x in d8:
  for y1 in d8[::-1]:
    for y2 in d8[::-1]:
      n = int( f'36{x}53', 8 ) - int( f"4{y1}{y2}3", 8 )
      if n > 0 and not done:
        print( n )
        done = True

