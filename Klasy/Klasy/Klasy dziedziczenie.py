class Character:
    def __init__(self, _name, _surname, _race):
        self.name = _name
        self.surname = _surname
        self.race = _race
    def fullname(self):
        print( '{} {}'.format(self.name, self.surname))

class Mage (Character):
    speciality = ''
    power = 0

    def __init__(self, _name, _surname, _race, _age):
        super().__init__(_name, _surname, _race)
        self.age = _age

    def fullinfo(self):
        print('{} {} {} {}'.format(self.name, self.surname, self.race, self.age))
    
    def addPower(self):
        self.power = self.power + 1

pl1 = Character('Krzysio', 'Waligóra', 'Elf')
pl2 = Character('Borys', 'Zamorski', 'Human')

pl1.fullname()
Character.fullname(pl1)

mg1 = Mage('Bartosz', 'Magiczny', 'Ork', 500)
mg1.fullname()
mg1.fullinfo()
Character.fullname(mg1)
print(mg1.speciality, mg1.power)
mg1.addPower()
print(mg1.power)

print('\n')
print(isinstance(mg1, Character))
print(isinstance(mg1, Mage))

print(isinstance(pl1, Character))
print(isinstance(pl1, Mage))

print(issubclass(Mage, Character))


