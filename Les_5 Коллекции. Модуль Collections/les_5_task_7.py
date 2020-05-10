from collections import ChainMap

# сначала построим несколько словарей
# у нас будет возможность построить из них цепочку
d1 = {'a': 2, 'b': 4, 'c': 5}
d2 = {'a': 10, 'b': 20, 'd': 40}

d_map = ChainMap(d1, d2)  # важен порядок элементов
print(d_map)

d2['a'] = 100
print(d_map)