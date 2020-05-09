from collections import Counter

a = Counter()
b = Counter('abrakadabra')
c = Counter({'red': 2, 'blue': 4})
d = Counter(cats=4, dogs=5)

print(a, b, c, d, sep='\n')
