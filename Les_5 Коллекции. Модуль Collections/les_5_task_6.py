from collections import namedtuple

# начнем с обычного кортежа
# создадим персонажа игры
# имя, раса, здоровье, мана, сила
hero_1 = ('Aaz', 'Izverg', 100, 0.0, 250)
print(hero_1[4])


# это неудобно, так как всегда нужно помнить названия параметров
# создадим класс персонаж
class Person:
    def __init__(self, name, race, heath, mana, streinght):
        self.name = name
        self.race = race
        self.heath = heath
        self.mana = mana
        self.stereinght = streinght


hero_2 = Person('Aaz', 'Izverg', 100, 0.0, 250)
print(hero_2.mana)

New_person = namedtuple('New_person', 'name, race, heath, mana, streinght')
hero_3 = New_person('Aaz', 'Izverg', 100, 0.0, 250)
print(hero_3.race)

prop = ['name', 'race', 'heath', 'mana', 'streinght']
New_person_1 = namedtuple('New_person_1', prop)
hero_4 = New_person_1('Aaz', 'Izverg', 100, 0.0, 250)
print(hero_4.race)
