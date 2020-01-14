class Character:
    def __init__(self, _name, _surname, _race):
        self.name = _name
        self.surname = _surname
        self.race = _race
    def fullname(self):
        print( '{} {}'.format(self.name, self.surname))

pl1 = Character('Krzysio', 'Waligóra', 'Elf')
pl2 = Character('Borys', 'Zamorski', 'Human')

pl1.fullname()
Character.fullname(pl1)
