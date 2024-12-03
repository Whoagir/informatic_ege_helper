from itertools import permutations

words = set([''.join(w) for w in permutations("ОДЕКОЛОН")])
words = [w for w in words if "ОО" not in w]
print( len(words) )