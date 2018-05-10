"""
pistol round
shotty* round
rifle round
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


class CarBattery(QuestItem):
    def __init__(self, name, points, description):
        super(QuestItem, self).__init__(self, name, points, description)
        self.points = points
        self.in_car = False

    def put_in_car(self):
        print('You hook up the poles to the cables and the car is ready to roll')
        self.in_car = True


class Weapon(Item):
    def __init__(self, name, description, damage, size):
        super(Weapon, self).__init__(name, description, damage, size)
        self.damage = damage


class FryingPan(Weapon):
    def __init__(self, name, description, damage, size):
        super(Weapon, self).__init__(name, description, damage, size)
        self.damage = damage

    def throw(self):
        print('You YEET that pan so hard it hits the target and they are knocked out stone cold')

    def whack(self):
        print('You smack the target so hard the pan breaks it')


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


class Gun(Weapon):
    def __init__(self, name, description, damage, size):
        super(Weapon, self).__init__(name, description, damage, size)
        self.mag = 'magazine'

    def fire(self):
        print('You pull the trigger and the end of your %s explodes in a glorious, deadly flame' % self.name)

    def reload(self):
        print('You slam a fresh new magazine into the %s' % self.name)


class Grenade(Weapon):
    def __init__(self, name, description, damage, size, blast_type, blast_size):
        super(Weapon, self).__init__(name, description, damage, size)
        self.type = blast_type
        self.blast = blast_size
        self.pin = True
        self.spoon_dropped = False
        self.thrown = False

    def pull_pin(self):
        print('You pull the pin on the grenade, but hold the spoon in place')
        self.pin = False

    def drop_spoon(self):
        if self.pin is False:
            print('You drop the spoon and the grenade will explode in 5 seconds')
        if self.pin is True:
            print('You cannot drop the spoon until you pull the pin')

    def throw(self):
        print('You throw the grenade as far away from you as you can')
        self.thrown = True


class Flashbang(Grenade):
    def __init__(self, name, description, damage, size, stun_time):
        super(Grenade, self).__init__(name, description, damage, size)
        self.stun = stun_time


class Frag(Grenade):
    def __init__(self, name, description, damage, size):
        super(Grenade, self).__init__(name, description, damage, size)


class Rifle(Gun):
    def __init__(self, name, description, damage, size, round):
        super(Weapon, self).__init__(name, description, damage, size)
        self.damage = damage
        self.round = round


class Pistol(Gun):
    def __init__(self, name, description, damage, size, round):
        super(Weapon, self).__init__(name, description, damage, size)
        self.damage = damage
        self.round = round


class Shotgun(Gun):
    def __init__(self, name, description, damage, size, round):
        super(Weapon, self).__init__(name, description, damage, size)
        self.damage = damage
        self.round = round


class SMG(Gun):
    def __init__(self, name, description, damage, size, round):
        super(Weapon, self).__init__(name, description, damage, size)
        self.damage = damage
        self.round = round


class R4C(Rifle):  # 39 damage, rifle round
    def __init__(self, name, description, damage, size):
        super(Rifle, self).__init__(name, description, damage, size)
        self.damage = damage and 39


class SuperNova(Shotgun):  # 48 damage, shotty* round
    def __init__(self, name, description, damage, size):
        super(Shotgun, self).__init__(name, description, damage, size)
        self.damage = damage and 48
        self.mag = 'set of shells'

    def fire(self):
        print('You pull the trigger and the end of your %s explodes in a glorious, deadly flame, and you rack the pump'
              '' % self.name)

    def reload(self):
        print('You slam a fresh set of shells into the %s' % self.name)


class D50(Pistol):  # 71 damage, pistol round
    def __init__(self, name, description, damage, size):
        super(Pistol, self).__init__(name, description, damage, size)
        self.damage = damage and 71


class SIX12(Shotgun):  # 45 damage, shotty* round
    def __init__(self, name, description, damage, size):
        super(Shotgun, self).__init__(name, description, damage, size)
        self.damage = damage and 45
        self.mag = 'drum'

    def reload(self):
        print('You slam a new drum into the %s' % self.name)


class MK14(Rifle):  # 60 damage, rifle round
    def __init__(self, name, description, damage, size):
        super(Rifle, self).__init__(name, description, damage, size)
        self.damage = damage and 60


class L85A2(Rifle):  # 47 damage, rifle round
    def __init__(self, name, description, damage, size):
        super(Rifle, self).__init__(name, description, damage, size)
        self.damage = damage and 60


class M1A1Carbine(Rifle):  # 40 damage, rifle round
    def __init__(self, name, description, damage, size):
        super(Rifle, self).__init__(name, description, damage, size)
        self.damage = damage and 40


class Colt1911(Pistol):  # 58 damage, pistol round
    def __init__(self, name, description, damage, size):
        super(Pistol, self).__init__(name, description, damage, size)
        self.damage = damage and 58


class T5smg(SMG):  # 30 damage, pistol round
    def __init__(self, name, description, damage, size):
        super(SMG, self).__init__(name, description, damage, size)
        self.damage = damage and 30


class TVRemote(Item):
    def __init__(self, name, weight, value, description, battery):
        super(TVRemote, self).__init__(name, weight, value, description)
        self.battery = battery

    def change_channel(self):
        if self.battery is False:
            print('The remote is dead.')
        if self.battery is True:
            print('You change the channel')


class TV(Item):
    def __init__(self, name, weight, value, description):
        super(TV, self).__init__(name, weight, value, description)
        self.channel = 1

    def watch(self):
        if self.channel == 1:
            self.channel = 1
            print("You watch the news")
        if self.channel == 2:
            self.channel = 2
            print("You watch the weather")
        if self.channel == 3:
            self.channel = 3
            print("You watch the sports channel")
        if self.channel > 3:
            self.channel -= 3
        if TVRemote.change_channel:
            self.channel += 1


six12one = SIX12('SIX12 Modular Shotgun', 'A bullpup 12-gauge shotgun with a revolving six-shot drum', 45, 10)
six12one.fire()
six12one.reload()
r4c1 = R4C('R4C', 'A lightweight assault rifle with a 30-round magazine', 39, 15)
r4c1.fire()
r4c1.reload()
sprnva1 = SuperNova('Benelli SuperNova', 'A compact tactical pump-action shotgun with good recoil control', 48, 15)
sprnva1.fire()
sprnva1.reload()


"""
remote1 = TVRemote('TV Remote', 1, None, 'There are buttons to change the channel', True)
tv1 = TV('TV', 51, None, 'It is an old TV with bunny ear antennae on it.')

tv1.watch()
remote1.change_channel()
tv1.watch()
remote1.change_channel()
tv1.watch()
print('\nend of test one\n')
#  test 1, works

tv1.watch()
remote1.change_channel()
remote1.change_channel()
tv1.watch()
print('\nend of test two\n')
#  test 2, does not work as intended (tv.watch once = does not say 'you watch the news'
#  if you put tv.watch twice at the top it works as intended. reason unknown
"""
