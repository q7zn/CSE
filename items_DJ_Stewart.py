#  grenade archetypes (smokes / flash / of course the frags too)
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


class QuestItem(Item):
    def __init__(self, name, points, description):
        super(QuestItem, self).__init__(name, points, description)
        self.points = points

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
    def __init__(self, name, weight, value, description, defense_mod):
                super(Armor, self).__init__(name, weight, value, description)
                self.defense = defense_mod
