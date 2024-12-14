with open('26-98.txt') as F:
  N, S = map( int, F.readline().split() )
  data = []
  for i in range(N):
    price, catg = F.readline().split()
    price = int(price)
    if 'C' in catg:
      discount = 0.1*price if 'A' in catg else 0.2*price
    else:
      discount = 0
    data += [ (price-discount, 'C' in catg) ]

data.sort()

money = 0
discountPrices = []
i = 0
while i < len(data) and money+data[i][0] <= S:
  price, discount = data[i]
  money += price
  if discount:
    discountPrices.append( price )
  i += 1

print( i, round(money) )

i -= 1
money -= price
if discount:
  discountPrices = discountPrices[:-1]

while i < len(data) and money+data[i][0] <= S:
  price, discount = data[i]
  if discount:
    discountPrices.append( round(price) )
  i += 1

print( round( max(discountPrices) ) )



