# task_4
import cProfile


def test_fib(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Test {i} OK')


def fib_list(n):
    fib_l = [None] * 1000
    fib_l[:2] = [0, 1]

    def _fib_list(n):
        if fib_l[n] is None:  # проверка, вычисляли ли мы уже число или нет
            fib_l[n] = _fib_list(n - 1) + _fib_list(n - 2)
        return fib_l[n]

    return _fib_list(n)


'''
task_5._fib_list(10)
1000 loops, best of 5: 13.9 usec per loop

task_5._fib_list(20)
1000 loops, best of 5: 18.3 usec per loop

task_5._fib_list(100)
1000 loops, best of 5: 69 usec per loop

task_5._fib_list(200)
1000 loops, best of 5: 114 usec per loop

task_5._fib_list(500)
1000 loops, best of 5: 381 usec per loop
'''
