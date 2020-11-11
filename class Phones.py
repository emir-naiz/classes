class Phones:
    def __init__(self, name, model, color, memory, price, status, touchpad, screen, sound, battery_life):
        self.name = name
        self.model = model
        self.color = color
        self.memory = 32
        self.price = ''
        self.status = ''
        self.battery_life = 500
        self.touchpad = 5
        self.screen = False
        self.sound = False

    def description(self):
        print(f"Название телефона - {self.name}, модель - {self.model}, цвет - {self.color}, память телефона - {self.memory} состояния телефона - {self.status}, цена - {self.price}")
    def touchpad(self, button):
        if button < 5:


iphone = Phones('iPhone', 'SE', 'White')
iphone.memory = 32
iphone.status = 'New'
iphone.price = 45000






