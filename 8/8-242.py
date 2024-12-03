from itertools import permutations

def valid( s ):
  sd = ""
  for c in s:
    if c in "АЕИОУЫЭЮЯ":
      sd += "g"
    else:
      sd += "s"
  return "gg" in sd or "ss" in sd

base = "АТТЕСТАТ"
words = [ "".join(w) for w in permutations(base) ]
words = [ w for w in words if valid(w) ]

print( len(set(words)) )