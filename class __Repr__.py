class Cat:
    def __init__(self, name):
        self.name = name
        self.color = 'white'

    def __repr__(self):
        return f'{self.name} {self.color}'


cat_list = ['Barsik', 'Murka', 'Snow', 'Vasya', 'Maya', 'Simba', 'Star']
super_cat_list = []
for cat in cat_list:
    new_cat = Cat(cat)
    super_cat_list.append(new_cat)
print(super_cat_list)