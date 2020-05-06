from random import randint
import cProfile

'''
les_3_task_2
2. Во втором массиве сохранить индексы четных элементов первого массива. 
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, 
второй массив надо заполнить значениями 0, 3, 4, 5 (помните, что индексация начинается с нуля), 
т. к. именно в этих позициях первого массива стоят четные числа.
'''


def save_index(n):
    list_1 = [randint(1, 100) for _ in range(n)]
    # print(f'list_1 {list_1}')

    list_2 = []
    for i in enumerate(list_1):
        if i[1] % 2 == 0:
            list_2.append(i[0])
    # print(f'list_2 {list_2}')


# cProfile.run('save_index(100)')
'''
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 les_3_task_2.py:13(save_index)
        1    0.000    0.000    0.000    0.000 les_3_task_2.py:14(<listcomp>)
      100    0.000    0.000    0.000    0.000 random.py:174(randrange)
      100    0.000    0.000    0.000    0.000 random.py:218(randint)
      100    0.000    0.000    0.000    0.000 random.py:224(_randbelow)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       60    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
      100    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
      124    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
'''

'''
"les_3_task_2.save_index(10)"
1000 loops, best of 5: 18.3 usec per loop

"les_3_task_2.save_index(20)"
1000 loops, best of 5: 45.6 usec per loop

"les_3_task_2.save_index(100)"
1000 loops, best of 5: 186 usec per loop

"les_3_task_2.save_index(500)"
1000 loops, best of 5: 1.03 msec per loop
'''