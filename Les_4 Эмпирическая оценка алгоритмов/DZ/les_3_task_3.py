import cProfile

'''
les_3_task_3
Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. 
Например, если введено число `3486`, надо вывести `6843`.
'''


def revert_number(n):
    revert = ""
    for i in str(n):
        revert = i + revert

    # print(revert)


# cProfile.run('revert_number(100000)')

'''
"les_3_task_3.revert_number(10)"
1000 loops, best of 5: 755 nsec per loop

"les_3_task_3.revert_number(1234)"
1000 loops, best of 5: 869 nsec per loop

"les_3_task_3.revert_number(123456789)"
1000 loops, best of 5: 2.39 usec per loop
'''