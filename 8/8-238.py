from itertools import permutations

def valid( s ):
  sd = ""
  for c in s:
    if c in "АЕИОУЫЭЮЯ":
      sd += "g"
    else:
      sd += "s"
  return "gg" not in sd and "ss" not in sd

base = "ВЕРЕТЕНО"
words = [ "".join(w) for w in permutations(base) ]
words = [ w for w in words if valid(w) ]

print( len(set(words)) )