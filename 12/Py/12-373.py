
def val(s):
  return sum(map(int, s))

def alg( s, verbose = 0 ):
  if verbose: print(s, val(s))
  while '3' in s:
    if '342' in s:
      s = s.replace('342', '4123', 1)  # +1
    if '34' in s:
      s = s.replace('34', '413', 1)    # +1
    if '32' in s:
      s = s.replace('32', '13', 1)     # -1
    if '33' in s:
      s = s.replace('33', '424', 1)    # +4
    if verbose: print(s, val(s))
  return s

s = '3' + 18*'424' + 3*'422' + '42' + '3'
   #      18*(+1+1)   3*(+1-1)  1*3
r = alg(s)

print( val(r) )




