"""
car battery
AA battery
R4C rifle, SuperNova shotgun, D50 pistol SIX12 Modular shotgun, MK14 Marksman
Rifle, M1A Carbine, Colt 1911 pistol, T-5 SMG
frying pan (weapon) (easter egg steering wheel?)
grenade archetypes (smokes / flash / of course the frags too)
Adrenaline
"""


class Item(object):
    def __init__(self, name, weight, value, description):
        self.name = name
        self.weight = weight
        self.value = value
        self.description = description

    def drop(self):
        print("You drop the %s" % self.name)

    def pick_up(self):
        if self.weight < 51:
            print("You pick up the %s" % self.name)
        else:
            print("You try to pick up the %s, but it is too heavy." % self.name)


class QuestItem(Item):
    def __init__(self, name, points, description):
        super(QuestItem, self).__init__(self, name, points, description)
        self.points = points


class Weapon(Item):
    def __init__(self, name, description, damage, size):
        super(Weapon, self).__init__(name, description, damage, size)
        self.damage = damage


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
    def __init__(self, name, weight, value, description, defense_mod):
                super(Armor, self).__init__(name, weight, value, description)
                self.defense = defense_mod


class TVRemote(Item):
    def __init__(self, name, weight, value, description, battery, inventory):
        super(TVRemote, self).__init__(name, weight, value, description)
        self.battery = battery
        self.inventory = inventory

    def use(self):
        if self.battery is False:
            print('The remote is dead.')
        if self.battery is True:
            print('You change the channel')


class TV(Item):
    def __init__(self, name, weight, value, description):
        super(TV, self).__init__(name, weight, value, description)