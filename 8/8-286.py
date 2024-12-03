from itertools import product

allWords = set()
for x in product('САМОКАТ', repeat=7):
  s = ''.join(x)
  if s.count('САМ') == 1:
    pos = s.find('САМ')
    if pos not in [0,4]:
      if s[pos-1] in 'АО' and s[pos+3] == s[pos-1]:
        #print(s)
        allWords.add(s)

print( len(allWords) )
