import cProfile

'''
les_3_task_2
Посчитать четные и нечетные цифры введенного натурального числа. 
Например, если введено число `34560`, в нем 3 четные цифры (`4`, `6` и `0`) и 2 нечетные (`3` и `5`).
'''


def parity_or_not(n):
    parity = 0
    non_parity = 0
    for i in str(n):
        i = int(i)
        if i % 2 == 0:
            parity += 1
        else:
            non_parity += 1

    # print(f'Число чётных чисел = {parity}\nЧисло нечётных чисел = {non_parity}')


cProfile.run('parity_or_not(1000)')

'''
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 les_2_task_2.py:13(parity_or_not)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


"les_3_task_2.parity_or_not(123456)"
1000 loops, best of 5: 4.28 usec per loop

"les_3_task_2.parity_or_not(1234567)"
1000 loops, best of 5: 3.47 usec per loop

"les_3_task_2.parity_or_not(12345678)"
1000 loops, best of 5: 3.33 usec per loop

'''
