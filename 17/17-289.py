data = [ int(x) for x in open("17-288.txt") ]
N = len(data)
count, mi = 0, None
for i in range(N-3):
  quad = data[i:i+4]
  if any( abs(x) % 10 == 3 for x in quad ) and \
     not any( abs(x) % 7 == 3 for x in quad ):
    count += 1
    diff = max(quad) - min(quad)
    if mi == None or diff < mi:
      mi = diff

print( count, mi )
