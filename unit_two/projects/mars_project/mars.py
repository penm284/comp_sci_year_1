import random

class People ():
    def __init__(self, name = None, strength= None, fatiuge= None, knowledge=None, money=None, spaceship=None, food = None, weapon = None, fuel = None, shield = None):
        self.strength = strength
        self.fatiuge = fatiuge
        self.knowledge = knowledge
        self.money = money
        self.spaceship = spaceship
        self.food = food
        self.weapon = weapon
        self.fuel = fuel
        self.shield = shield

    def __repr__(self):
        return repr((self.name, self.strength, self.fatiuge, self.knowledge, self.money, self.spaceship, self.food, self.weapon, self.fuel, self.shield))

def chose_character ():
    person = input ("Who would you like to be? Elon Musk, Neil Armstrong, or Buzz Lightyear \n")
    if person == "Elon Musk":
        ElonMusk = People()
        ElonMusk.name = "Elon Musk"
        ElonMusk.strength= 3
        ElonMusk.fatigue = 2
        ElonMusk.knowledge = 10
        ElonMusk.money = 130000
        ElonMusk.spaceship = 8
        return ElonMusk
    elif person == "Neil Armstrong":
        NeilArmstrong = People()
        NeilArmstrong.name = "Neil Armstrong"
        NeilArmstrong.strength= 7
        NeilArmstrong.fatigue = 9
        NeilArmstrong.knowledge = 8
        NeilArmstrong.money = 110000
        NeilArmstrong.spaceship = 3
        return NeilArmstrong
    elif person == "Buzz Lightyear":
        BuzzLightyear = People()
        BuzzLightyear.name = "Buzz Lightyear"
        BuzzLightyear.strength= 10
        BuzzLightyear.fatigue = 7
        BuzzLightyear.knowledge = 3
        BuzzLightyear.money = 100000
        BuzzLightyear.spaceship = 6
        return BuzzLightyear
    else:
        print ("couldn't understand what you said")
        chose_character ()

def how_much (item, units):
    how_much = int(input("How much " + item + " do you wanna buy in " + units + "?"))
    return how_much

def store(character):
    print ("You have $" + str(character.money))
    stuff_to_buy = input ("what do you want to buy: food, weapons, fuel, shield - make sure you buy enough of each to survive \n")
    cost = 0
    if stuff_to_buy == "food":
        ammount = how_much("food", "pounds")
        temp = cost
        cost = cost + (ammount *40)
        if character.money < cost:
            print ("sorry, you don't have enough money")
            cost = temp
        character.food = ammount
    elif stuff_to_buy == "weapons":
        print ("Which weapon do you want to buy \n")
        print ("Ray gun: 10,000")
        print  ("Sword: 8,000")
        print  ("Machine gun: 5,000")
        weapon = input ()
        temp = cost
        if weapon == "Ray gun":
            cost = cost + 10000
            character.weapon = "Ray gun"
        elif weapon == "Asteroid gun":
            cost = cost + 20000
            character.weapon = "Sword"
        elif weapon == "Machine gun":
            cost = cost + 5000
            character.weapon = "Machine gun"
        if character.money < cost:
            print ("sorry, you don't have enough money")
            cost = temp
    elif stuff_to_buy == "fuel":
        ammount = how_much("fuel", "liters")
        temp = cost
        cost = cost + (ammount *60)
        if character.money < cost:
            print ("sorry, you don't have enough money")
            cost = temp
        character.fuel = ammount
    elif stuff_to_buy == "shield":
        temp = cost
        cost = cost + 30000
        if character.money < cost:
            print ("sorry, you don't have enough money")
            cost = temp
        character.shield = True
    character.money = int(character.money) - cost
    buy_more = input ("Would you like to buy more things from the store? (Y/N)")
    if buy_more == "Y":
        store(character)
    else:
        return

def alien_attack (character):
    print ("\n")
    print (character.name + " you are being attacked by aliens!! \n")
    print ("Captain, you can: ")
    print ("a) Fight them")
    print ("b ) Run away")
    print ("c) Bribe the aliens - costs $50,000")
    decision = input()
    if decision == "a":
        if character.weapon == "Ray gun":
            print ("Good job. The aliens have been defeated, but you did lose some health")
            character.strength = character.strength - 2
            character.fatigue = character.fatigue - 1
            if character.strength == 0 or  character.fatigue == 0:
                print ("You lost too much health and died. Mission failed")
                return False
            return True
        else:
            print ("Your weapon was not powerful enough to fight of the alien. Mission Failed")
            return False
    elif decision == "b":
        if character.fatigue > 3 and character.strength > 3:
            print ("Good job. You escaped the aliens unscathed!")
            return True
        else:
            print ("You were not strong enough to outrun the aliens. Mission Failed")
            return False
    elif decision == "c":
        if character.money >= 50000:
            print ("It cost you $50,000, but you managed to bribe the aliens")
            character.money = character.money - 50000
            return True
        else:
            print ("You did not have enough money. Mission Failed")
            return False

def asteroids (character):
    print ("\n")
    print ("Oh no!!! There are asteroids coming up ahead")
    if character.shield == True:
        print ("You are lucky you bought an asteroid shield. You are unscathed!")
        return True
    else:
        print ("You did not have a shield so you lost quite a bit of health")
        character.strength = character.strength -3
        character.food = character.food-200
        if character.strength == 0 or character.food == 0:
            print ("You lost too much strength and supplies. Mission failed")
            return False

def ship_breakdown (character):
    print ("\n")
    print ("There is an error with your ship! What do you want to do")
    print ("a) try to repair ship")
    print ("b) eject on the emergency escape pod")
    print ("c) pay your engineers to fix it - cost $100,000")
    decision = input()
    if decision == "a":
        if character.knowledge > 5:
            print ("Good think you know how to repair ships! You survived this one")
            return True
        else:
            print ("Uh oh, you do no possess enough knowledge to repair this ship. Mission failed")
            return False
    elif decision == "b":
        if character.strength > 5 and character.fatigue > 5:
            print ("You made it on the pod and have enough energy to survive!")
            return True
        else:
            print ("You do not have enough strength or fatigue. Mission failed")
            return False
    elif decision == "c":
        if character.money >= 100000:
            character.money = character.money - 100000
            print ("Ship repaired!")
            return True
        else:
            print ("You don't have enough money. Mission failed")
            return False

def alien_on_board (character):
    print ("\n")
    print ("Oh no!!! An alien has boarded the ship!")
    print ("a) Fight them")
    print ("b) eject on the emergency escape pod")
    print ("c) bribe them cost $75,000")
    if character.weapon == "Sword":
        print ("Good thinking... Buying a sword was a great idea. Both you and your ship remain are unharmed!")
        return True
    else:
        print ("Your weapon was not meant for this situation. After a hard fought battle, you have slayed the alien, however, you've lost health and fatigue.")
        character.health = character.health -5
        character.fatigue = character.fatigue-10
        if character.health == 0 or character.fatigue == 0:
            print ("You've lost too much health and have become utterly fatigued. Mission failed.")
            return False

def go_to_mars(character):
    print ("Ok time for take off captain!")
    if character.fuel < 500:
        print ("Uh oh, you don't have enough fuel. Mission failure")
        return
    print ("congradulations, you are now in orbittt!")
    character.fatigue = character.fatigue - 1
    character.strength = character.strength - 1
    possible_outcomes = [asteroids(character), ship_breakdown(character), alien_attack(character), alien_on_board(character)]
    outcome = random.randint(0,3)
    if possible_outcomes[outcome] == False:
        return
    else:
        print ("Good job, you made it to mars!")
        return





character = chose_character()
store(character)
go_to_mars(character)
