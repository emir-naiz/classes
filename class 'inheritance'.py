# ООП - парадигма программирования
# делится на три принципа: "Наследования", "Инкапсуляция", "Полиморфизм"

#Наследования
class Planet:
    def __init__(self, name, position):
        self.name = name
        self.form = 'shape'
        self.position = position
        self.temp = 0
        self.size = 0

    def description(self):
        print(f'Название - {self.name}, форма - {self.form}, позиция - {self.position}, температура - {self.temp}, размер - {self.size}')

class Mercury(Planet):
    def __init__(self, position, name = 'Mercury'):
        super().__init__(name, position)
        self.temp = 120
        self.size = 'small'

class Jupyter(Planet):
    def __init__(self, position, name = 'Jupyter'):
        super().__init__(name, position)
        self.temp = 240
        self.size = 'great'
        self.brilliant_rain = True

    def description(self):
        print(f'Название - {self.name}, форма - {self.form}, позиция - {self.position}, температура - {self.temp}, размер - {self.size}, дождь из бриллиантов - {self.brilliant_rain}')

class Saturn(Planet):
    def __init__(self, position, name = 'Saturn'):
        super().__init__(name, position)
        self.temp = -100
        self.size = 'middle'
        self.rings = True
        self.count_rings = 7

    def description(self):
        print(
            f'Название - {self.name}, форма - {self.form}, позиция - {self.position}, температура - {self.temp}, размер - {self.size}, кольца - {self.rings}, колл-во - {self.count_rings}')


mercury = Mercury('Solar system')
mercury.description()

jup = Jupyter('Solar system')
jup.description()

saturn = Saturn('Solar system')
saturn.description()