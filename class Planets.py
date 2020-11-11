class Planet:
    def __init__(self, name, size, color):
        self.name = name
        self.size = size
        self.color = color
        self.temp = -999
        self.oxygen = False
        self.water = False
        self.humanity = False

    def description(self):
        print(f"Название планеты - {self.name}, размер - {self.size}, цвет - {self.color}, Температура = {self.temp}. "
              f"Наличие воздуха - {self.oxygen}, воды = {self.water}, человечества - {self.humanity}")

    def set_humanity(self):
        self.humanity = True
        self.oxygen = True
        self.water = True
        self.temp = 15

    def population(self, people):
        if self.humanity and self.water and self.oxygen:
            if people > 0:
                self.humanity = people
            else:
                print('Не балуйся!')
        else:
            print('Жизни нет!')

earth = Planet('Earth', 20, 'Blue')
earth.set_humanity()
earth.population(2)

earth.description()
