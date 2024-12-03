from itertools import permutations

vars = []
def valid( s ):
  sd = ""
  for c in s:
    if c in "АЕИОУЫЭЮЯ":
      sd += "g"
    else:
      sd += "s"
  vars.append( sd )
  return "gg" in sd or "ss" in sd

base = "ПРЕПАРАТ"
words = [ "".join(w) for w in permutations(base) ]
words = [ w for w in words if valid(w) ]

print( len(set(vars)) )
print( len(words) )
print( len(set(words)) )