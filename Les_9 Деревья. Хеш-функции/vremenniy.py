import collections


class Leaf:
    """ Вспомогательный класс Лист для создания дерева Хаффмана """

    def __init__(self, key: str, value: int):
        """
        :param key: буква из кодируемой строки
        :param value: частота буквы в строке
        """
        self.key = key
        self.value = value


class Node:
    """ Вспомогательный класс Узел для построения дерева Хаффмана """

    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


class Haffman:
    """ Класс, реализующий сжатие и восстановление строки по алгоритму Хаффмана """
    _data: list

    def __init__(self):
        """
        _code_table: таблица кодирования: key=буква, value=двоичный код
        _data: список для преобразования из строки в дерево
        _real_str: строка для кодирования
        """
        self._code_table = dict()
        self._data = []
        self._real_str = ''

    def _make_list(self, real_str):
        """
        Формируем упорядоченный по убыванию список объектов класса Leaf
        :param real_str:
        :return:
        """
        counter = dict(collections.Counter(real_str))
        counter = collections.OrderedDict(sorted(counter.items(), key=lambda k: k[1], reverse=True))
        for key, value in counter.items():
            self._data.append(Leaf(key, value))
        return True

    def _haffmans_tree(self):
        """ Функция формирует из списка объектов класса Leaf бинарное дерево по алгоритму Хаффмана """
        while len(self._data) > 2:
            b, a = self._data.pop(0), self._data.pop()
            spam = Node(a.value + b.value, a, b)
            if spam.value > self._data[0].value:
                self._data.insert(0, spam)
            elif spam.value < self._data[-1].value:
                self._data.append(spam)
            else:
                for i in range(1, len(self._data)):
                    if self._data[i - 1].value >= spam.value > self._data[i].value:
                        self._data.insert(i, spam)
                        break
        self._data = Node(self._data[0].value + self._data[1].value, self._data[0], self._data[1])

    def _haffman_recursion(self, data: Node, code=''):
        """ Рекурсивный обход дерева и построение таблицы кодирования """
        if isinstance(data, Node):
            self._haffman_recursion(data.left, code=code + '0')
            self._haffman_recursion(data.right, code=code + '1')
        elif isinstance(data, Leaf):
            self._code_table[data.key] = code

    def _encode(self):
        """
        Преобразование из строки в двоичный код
        Имитация со строковыми '0' и '1' для демонстрации работы
        """
        result = []
        for char in self._real_str:
            result.append(self._code_table[char])
        return ''.join(result)

    def encode(self, real_str):
        """
        Основной метод преобразования строки в код по алгоритму Хаффмана
        :param real_str: строка
        :return: code_str
        """
        self.__init__()
        self._real_str = real_str
        self._make_list(real_str)
        self._haffmans_tree()
        self._haffman_recursion(self._data)
        code_str = self._encode()
        return code_str

    def decode(self, code_str, code_table=None):
        """
        Декодирование строки из '0' и "1' на основе таблицы кодирования code_table
        Если code_table не передан, то испольуется получанная ранее таблица
        :param code_str:
        :param code_table:
        :return:
        """
        if code_table:
            self._code_table = code_table
        decode_table = {value: key for key, value in self._code_table.items()}
        result = []

        i = 0
        while i < len(code_str):
            j = i + 1
            while code_str[i:j] not in decode_table.keys():
                j += 1
            result.append(decode_table[code_str[i:j]])
            i = j

        real_str = ''.join(result)
        return result

    def get_table_code(self):
        """ Возвращает таблицу кодирования в виде словаря {буква: код} """
        if self._code_table:
            return self._code_table
        return False

    def get_real_string_code(self):
        """ Возвращает строку из '0' и '1' - реальный код строки для кодирования """
        if self._real_str:
            result = []
            for char in self._real_str:
                result.append(bin(ord(char))[2:].zfill(8))
            return ''.join(result)
        return False


if __name__ == '__main__':
    my_str = input('Введите строку для кодирования: ')
    haf = Haffman()
    code_s = haf.encode(my_str)
    print(haf.get_real_string_code())
    print(code_s)
    table = haf.get_table_code()
    print(table)
    real_1 = haf.decode(code_s, table)
    real_2 = haf.decode(code_s)
    print(real_1)
    print(real_2)
