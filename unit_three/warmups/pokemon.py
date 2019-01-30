class Pokemon():
    def __init__(self, hp, attack, name):
        self.hp = hp
        self.attack = attack
        self.name = name


    def battle(self, other):
        print(self.name, 'is in a fight with', other.name)
#pick an attack
        current_attack = input('what attack do you pick? tackle or slap')
        #set value based on choice
        if current_attack == 'tackle':
            current_attack = random.randit(0,25)
        else:
            current_attack = random.randit(0,50)
#attack on other change hp
        other.hp = other.hp - current_attack
        if other.hp > 0:
            return(other.battle(self))
        else:
            print(self.name,'won')

#instance of Pokemon
pablo = Pokemon(100, 25, 'pablo' )
teddy = Pokemon(100, 25, 'teddy' )
pablo.battle(teddy)
