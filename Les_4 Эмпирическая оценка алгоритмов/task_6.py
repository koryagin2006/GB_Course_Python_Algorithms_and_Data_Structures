import cProfile


def test_fib(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Test {i} OK')


def fib_loop(n):
    if n < 2:
        return n
    first, second = 0, 1
    for _ in range(2, n + 1):
        first, second = second, first + second
    return second


test_fib(fib_loop)

# task_6.fib_loop(10)
# 1000 loops, best of 5: 1.7 usec per loop

# task_6.fib_loop(100)"
# 1000 loops, best of 5: 12.1 usec per loop

# task_6.fib_loop(500)"
# 1000 loops, best of 5: 59.5 usec per loop

# task_6.fib_loop(50000)"
