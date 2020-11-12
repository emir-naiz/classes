# Расса
# имя, пол, тип(классификация), skill,
class Person:
    def __init__(self, name, sex, race):
        self.name = name
        self.sex = sex
        self.race = race
        self.weight = 0
        self.height = 0
        self.health = 0
        self.health = True
        self.attack = 5
        self.damage = 0
        self.defence = 0

    def description(self):
        print(f'Имя персонажа - {self.name}, пол - {self.sex}, раса - {self.race}, рост - {self.weight}, вес - {self.height}, '
              f'здоровье - {self.health}, урон - {self.damage}, защита - {self.defence}')

class Human(Person):
    def __init__(self, name = 'Adam', sex = 'male', race = 'human'):
        super().__init__(name, sex, race)
        self.weight = 180
        self.height = 85
        self.health = 1000
        self.damage = 120
        self.defence = 80
        self.warrior = True

    def description(self):
        print(f'Имя персонажа - {self.name}, пол - {self.sex}, раса - {self.race}, рост - {self.weight}, вес - {self.height},'
            f'здоровье - {self.health}, урон - {self.damage}, защита - {self.defence}, воин - {self.warrior}')
    def set_health(self, other_atack):
        if other_atack < self.health:
            print(f'Вы выиграли!, у вас осталось: {self.health}')
        else:
            print('Вы погибли!')


human = Human()
human.set_health(800)
human1 = Human()
human1.set_health(1000)
human.description()
