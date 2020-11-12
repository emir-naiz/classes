class Phone:
    def __init__(self, name, model, color, year, state):
        self.name = name
        self.model = model
        self.color = color
        self.year = year
        self.state = state
        self.memory = 32
        self.price = 1000
        self.battery = 0
        self.touchid = 5
        self.locked = False

    def description(self):
        print(f'Название телефона - {self.name}, модель - {self.model}, цвет - {self.color}, год - {self.year}, состояния телефона - {self.state}, цена - {self.price}')

    def set_battery(self,charge):
        if not self.locked:
            if 0 < charge <= 100:
                self.battery = charge
            else:
                print('Не балуйся')
        else:
            print('Обратитесь в салон!')

    def unlock(self,tries):
        if 0 < tries <= self.touchid:
            print('Вы зашли')
        else:
            self.locked = True
            print('Телефон заблокирован! Попробуйте через 30 сек')



iphone = Phone('iPhone', 'XII', 'White', 2019, 'New')
iphone.price = 1100
iphone.unlock(6)
iphone.set_battery(100)
iphone.description()




