from collections import defaultdict

list_1 = [('cat', 1), ('dog', 5), ('cat', 2), ('mouse', 1), ('dog', 1)]
c = defaultdict(list)
for k, v in list_1:
    c[k].append(v)
print(c)

list_2 = [('cat', 1), ('dog', 5), ('cat', 2), ('cat', 1), ('dog', 1), ('dog', 5)]
d = defaultdict(set)
for k, v in list_2:
    d[k].add(v)
print(d)

