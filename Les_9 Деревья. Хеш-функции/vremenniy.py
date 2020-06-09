# task_2
from binarytree import bst


def search(bin_search_tree, number, path=''):
    """
    :param bin_search_tree: дерево
    :param number: число
    :param path: нужно для сохранения пути
    """
    if bin_search_tree.value == number:
        return f'Число {number} обнаружено по следующему пути: \nКорень{path}'

    if number < bin_search_tree.value and bin_search_tree.left is not None:
        return search(bin_search_tree.left, number, path=f'{path}\nШаг влево')

    return f'Число {number} отсутствует в дереве'


bt = bst(height=5, is_perfect=False)
print(bt)
num = int(input('Введите число для поиска: '))
print(search(
    bin_search_tree=bt,
    number=num
))
