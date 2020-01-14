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

    def attack(self):
        print('Attacking!')

class FireMage (Mage):
    speciality = 'fire'
    power = 10

    def __init__(self, _name, _surname, _race, _age):
        return super().__init__(_name, _surname, _race, _age)

    def attack(self):
        print ('Attacking with fire!')

    def fullinfo(self):
        print('{} {} {} {} {} {}'.format(self.name, self.surname, self.race, self.age, self.speciality, self.power))

class HealerMage (Mage):
    speciality = 'healing'
    power = 15

    def __init__(self, _name, _surname, _race, _age):
        return super().__init__(_name, _surname, _race, _age)

    def attack(self):
        print ('I\'m a pacifist!')

    def fullinfo(self):
        print('{} {} {} {} {} {}'.format(self.name, self.surname, self.race, self.age, self.speciality, self.power))

h1 = HealerMage('Agata', 'Zielonogórska', 'Human', 25)
h1.attack()
Mage.attack(h1)

h1.power = 20
h1.fullinfo()
Mage.fullinfo(h1)
