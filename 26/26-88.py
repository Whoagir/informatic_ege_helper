with open("26-88.txt") as F:
   N = int( F.readline() )
   data = [ F.readline().rstrip() for i in range(N) ]

mask = '255.255.224.0'
int_mask = tuple( map(int, mask.split('.')) )

count = {}
for i in range(N):
  int_addr = list( map(int, data[i].split('.')) )
  for k in range(4):
    int_addr[k] &= int_mask[k]
  net = ".".join(map(str, int_addr))
  count[net] = count.get(net, []) + [data[i]]

count = list( count.items() )

count.sort( key = lambda x: (len(x[1]), x[0]), reverse = True )

for i in range(min(5,N)):
  print( count[i][0], len(set(count[i][1])), len(count[i][1]) )

