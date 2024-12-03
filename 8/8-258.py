from itertools import product
A = 'АИКЛМЬ'
words = list( "".join(word) for word in product(A, repeat = 6) )

def valid( s ):
  return s[0] == 'К' and s[-1] == 'Ь' and \
         all( s.count(c) == 1 for c in A ) and \
         words.index(s[::-1]) - words.index(s) == 26655

for i, word in enumerate(words):
  if valid(word):
    print( word, sum(map(int, str(i+1))) )
    break


