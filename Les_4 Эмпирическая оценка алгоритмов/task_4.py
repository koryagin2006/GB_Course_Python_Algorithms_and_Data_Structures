# task_4
import cProfile


def test_fib(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Test {i} OK')


def fib_dict(n):
    fib_d = {0: 0,
             1: 1}

    def _fib_dict(n):
        if n in fib_d:  # проверка, вычисляли ли мы уже число или нет
            return fib_d[n]
        else:
            fib_d[n] = _fib_dict(n - 1) + _fib_dict(n - 2)
        return fib_d[n]

    return _fib_dict(n)


cProfile.run('fib_dict(10)')
