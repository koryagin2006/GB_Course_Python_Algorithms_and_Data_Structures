from collections import deque
import random

array = [random.randint(-100, 100) for _ in range(10)]
print(array)

deq = deque()

for item in array:
    if item > 0:
        deq.append(item)
    elif item < 0:
        deq.appendleft(item)

print(list(deq))
