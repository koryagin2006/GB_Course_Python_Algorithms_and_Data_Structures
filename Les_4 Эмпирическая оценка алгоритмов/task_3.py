# task_3
import cProfile
import functools


def test_fib(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Test {i} OK')


@functools.lru_cache()
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

# "task_3.fib(10)"
# 1000 loops, best of 5: 134 nsec per loop

# "task_3.fib(100)"
# 1000 loops, best of 5: 225 nsec per loop
