import random
class Item(object):
    def __init__(self, name, weight, value, description):
        self.name = name
        self.weight = weight
        self.value = value
        self.description = description

    def drop(self):
        print("You drop the item")

    def pick_up(self):
        print("You pick up the item")


class Weapon(Item):
    def __init__(self, name, description, ammo_type, size):
        super(Weapon, self).__init__(name, description, ammo_type, size)
        self.round = ammo_type


class Wearable(Item):
    def __init__(self, name, weight, value, description):
        super(Wearable, self).__init__(name, weight, value, description)

    def put_on(self):
        print("You put on the %s" % self.name)

    def take_off(self):
        print("You take off the %s" % self.name)


class Backpack(Wearable):
    def __init__(self, name, weight, value, description, inventory):
        super(Backpack, self).__init__(name, weight, value, description)
        self.inventory = inventory

    def put_item_in(self):
        print("You put the %s in the backpack" % self.name)

    def take_item_out(self):
        print("You take the %s out of the backpack" % self.name)


class Armor(Wearable):
    def __init__(self):
    super(Armor, self).(name, weight)


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

    def attack(self, target):
        hit_chance = random.randint(1, 100)
        if hit_chance >= 50:
            target.take_damage()
        else:
            target.injure = False


class Terrorist(Character):
    def __init__(self, name, description, health, life, dialogue, status_effect, inventory, target):
        super(Terrorist, self).__init__(name, description, health, dialogue, status_effect, inventory, target)
        self.life = life

