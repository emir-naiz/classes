class Student:
    def __init__(self, name, laptop):
        self.name = name
        self.laptop = laptop
        self.height = 0
        self.sex = ''

    def __str__(self):
        return f"Name:{self.name}, Laptop:{self.laptop}, Height:{self.height}, Sex:{self.sex}"

vasya = Student("Vasya", "Acer")
vasya.height = 150
vasya.sex = 'male'
emir = Student("Emir", "Lenovo")
emir.height = 180
emir.sex = 'male'
baizak = Student("Baizak", "Razer")
baizak.height = 182
baizak.sex = 'male'
zarina = Student("Zarina", "Acer")
zarina.height = 170
zarina.sex = 'female'
aijan = Student("Aijan", "HP")
aijan.height = 165
aijan.sex = 'female'
nazira = Student("Nazira", "Asus")
nazira.height = 163
nazira.sex = 'female'
sultan = Student("Sultan", "iMac")
sultan.height = 175
sultan.sex = 'male'
print(vasya, emir, baizak, zarina, aijan, nazira, sultan)