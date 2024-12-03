from itertools import product

def valid( w ):
  return w[0] in "АБВГ" and \
         ((w[1] in "АЕ") == (w[0] in "АЕ")) and \
         (w[2] in "БВДЕ" and w[2] not in w[0]+w[1]) and \
         (w[3] in "БВГД" and w[3] not in w[1]+w[2])

count = 0
for w in product("АБВГДЕ", repeat=4):
  if valid(w):
    count += 1
    if ''.join(w) == "ГВЕД":
       print( count )
       break