import random
'''
must have:
name
health
pick up items
move(?)
attack
death
dialogue
interactions (use, push, etc)
character description
status effects (burn, poison, paralyze, hunger, etc)
take damage
'''

assignment = 'Create a character class. it must have 5 instance variables. All five instance variables must be used.'
'It must also have at least two methods.'


class Character(object):
    def __init__(self, name, description, health, dialogue, status_effect, inventory, target):
        self.name = name
        self.description = description
        self.health = health
        self.life = True
        self.dialogue = dialogue
        self.status_effect = status_effect
        self.inventory = inventory
        self.target = target

    def injure(self):
        self.health -= 40
        print('%s is hurt and loses 40 health' % self.name)

    def attack(self, target):
        hit_chance = random.randint(1, 100)
        if hit_chance >= 50:
            target.injure()
        else:
            target.injure = False

    def death(self):
        print('The %s dies' % self.name)


class Terrorist(Character):
    def __init__(self, name, description, health, life, dialogue, status_effect, inventory, target, enemy_spotted):
        super(Terrorist, self).__init__(name, description, health, dialogue, status_effect, inventory, target)
        self.life = life
        self.enemy_spotted = enemy_spotted
        self.health = 100

    def startle(self):
        print('The terrorist is caught off guard by you entering the room and is momentarily confused')

    def attack(self, target):
        print('The %s aims and fires at you' % self.name)


class Bomber(Terrorist):
    def __init__(self, name, description, health, life, dialogue, status_effect, inventory, target, enemy_spotted):
        super(Terrorist, self).__init__(name, description, health, dialogue, status_effect, inventory, target)
        self.life = life
        self.enemy_spotted = enemy_spotted
        self.health = 200
