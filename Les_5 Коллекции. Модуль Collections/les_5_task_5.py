from collections import OrderedDict, defaultdict, deque

'''
В лог-файл сервер добавляет ip-адреса, с которых пришел запрос.

Проанализоровать последние N адресов и сохранить в новый файл пары значений "ip-адрес - кол-во запросов".
- исключить локальные адреса (192.168.*.*)
- сохранить исходный порядок адресов
'''
# берем последние 3000 адресов

N = 3000
with open('big_log.txt', 'r', encoding='utf-8') as f:
    log = deque(f, N)  # сохраняем в очередь последние N значений

print(log)

# объявляем переменные
data = OrderedDict()
spam = defaultdict(int)

# избавляемся от символа перенова строки
for item in log:
    ip = item[:-1]  # для каждой строки оставляем все, кроме последнего символа

    if not ip.startswith('192.168'):
        spam[ip] += 1
        data[ip] = 1

print(spam)
print(data)

data.update(spam)  # добавляет в `data` ключи из `spam`
print(data)

with open ('data.txt', 'w', encoding='utf-8') as f:
    for key, value in data.items():
        f.write(f'{key} - {value}\n')
