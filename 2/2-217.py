print("a b c d")
tf = [0, 1]
for a in tf:
  for b in tf:
    for c in tf:
      for d in tf:
        if (not a) <= b and (not c  == b) and not d:
          print( b, a, c, d )