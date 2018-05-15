import random


class Room(object):
    def __init__(self, name, description, north, south, east, west, northwest, southwest, northeast, southeast, up,
                 down):
        self.description = description
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.southwest = southwest
        self.southeast = southeast
        self.northeast = northeast
        self.northwest = northwest
        self.up = up
        self.down = down

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


spawn = Room('Stair Alley', 'You wake up and find yourself in an alley with no recollection of what happened or why '
             'you\nare here. There are two sets of stairs, one to your north that leads up and one to your northwest\n'
             'that leads down.', 'side_stair', None, None, 'side_stair', 'basement_stair_out', None, None, None, None,
             None)
side_stair = Room('Side Staircase', 'You are on a staircase with two flights that leads up to the second and third '
                  'floor of a large building. \nYou stand on the second floor platform with  door to your west. The' 
                  'third floor door is to your south. There is an alley to your east.', None, 'storage_corridor',
                  'spawn', 'laundry_room', 'basement_entrance', None, None, None, None, None)
basement_stair_out = Room('Basement Staircase', 'You are on a staircase and there is a path that looks from your angle'
                          'to be a dead end to your south,\nthough it may be worth checking out.\nThere are stairs to'
                          ' your east and west.', None, 'briefing_room', 'side_stair', 'front_access', None, None, None,
                          None, None, None)
briefing_room = Room('Briefing Room', 'You are in a room with a few projectors and some desks.\nThere is a door leading'
                     ' outside to your east, and there is a hallway to your west.\nOne of the desks, the one to your '
                     'southwest, has a slightly open drawer.', 'basement_stair', None, 'basement_stair',
                     'basement_corridor', None, 'brief_desk', None, 'brief_desk', None, None)
front_access = Room('Front Access', 'A door wide enough for two people to enter side by side stands to your south. '
                    'There is a set of stairs leading down to your east.', None, 'main_corridor', 'basement_stair',
                    None, None, None, None, None, None, None)
garage_corridor = Room('Garage Hall', 'You are in a hallway that is not too long. There is a garage to your west, and '
                       'a long corridor to your east. There is a kitchen to your south.', None, 'kitchen',
                       'main_corridor', 'garage', None, None, None, None, None, None)
main_corridor = Room('Main Corridor', 'You are in a long hallway with many rooms on both sides. There is an exit to the'
                     ' outside to your north, a kitchen to your southwest, and another hallway to your west. There is a'
                     ' room with some TVs in another room to your northwest, and a kitchen to the southwest of your '
                     'position. There are stairs that lead up and down to the south. To the southeast is a room with a '
                     'table in the center, with quite a few creepy mannequins around it. Your gut tells you to avoid '
                     "that room, but you've never been one to listen to your gut.", 'front_access', 'main_stairs_1st',
                     None, 'garage_corridor', 'tv_room', 'kitchen', 'piano_lounge', 'dining_room', None, None)
main_stairs_1st = Room('Main Stairs', 'You are on a staircase that leads up to the second floor and down to the '
                       'basement. There is a hallway to your north with lots of doors in it', 'main_corridor', None,
                       None, None, None, None, None, None, 'main_stairs_2nd', 'main_stairs_bm')
brief_desk = Room('Briefing Room', 'You are in the corner of the briefing room, behind a desk. The drawer, upon closer'
                  'inspection, is locked, but could easily be forced open. You can move northeast outside, or northwest'
                  'to the corridor.', None, None, None, None, 'bm_corridor', None, 'basement_stair', None, None, None)
laundry_room = Room('Laundry Room', 'You are in a room with a wall directly in front of you that spans almost the whole'
                    ' way to the wall to your south. \nThere is an opening, however, to your southwest end of the '
                    'extended wall. There is a door to your east. There are many washing machines and related '
                    '\nappliances in the room. They might have something in them.', 'laundry_machines', None,
                    'side_stairs', None, None, 'laundry_inner', None, None, None, None)
laundry_inner = Room('Laundry Room', 'You have moved into the part of the laundry room that is closer to the inside of '
                     'the building. There is a wall that extends from the north end of the room almost to the south '
                     'wall, but the there is an opening. It looks odd from this side, almost like it was blown open by'
                     " a breach charge. You do not know why you know what a breaching charge's explosion would look "
                     "like. There is a path that leads to the outer part of the room to the southwest and a path into "
                     'a bedroom on your west.', None, None, None, 'master_bed', None, 'laundry_room', None, None, None,
                     None)
storage_corridor_e = Room('Storage Corridor East', 'You are in a long hallway with a sharp turn in it to your west. You'
                          'cannot see around the corner. There is a door that leads outside and to stairs going down to'
                          ' your east. You can go west down the hall or south into a work area. There is a camera in '
                          'the corner of the hall.', None, 'workshop', 'side_stair', 'storage_corridor_nw', None, None,
                          None, None, None, None)
storage_corridor_nw = Room('Storage Corridor Northeast', 'You are in the corner of the hallway. You can see down the '
                           'hall to the east and to the south. There is a room to your west with a bunch of things that'
                           ' look like place mats. There is more hallway to your south.', None, 'storage_corridor_s',
                           'storage_corridor_e', 'mat_depot', None, None, None, None, None, None)
# test
storage_corridor_s = Room('Storage Corridor South', 'You are at the south end of the hall and can see north. You see a '
                          'security camera to the north, and it is glowing red. You have a feeling you are being '
                          'watched. To your west lies a room with random things that seem to be fitting to the '
                          'environment, which to you appears to be an abandoned military base. There is a workshop to '
                          'your east and stairs leading down on your south.', 'storage_corridor_n', 'main_stairs_3rd',
                          'workshop', 'storage', None, None, None, None, None, None)
mat_depot = Room('Ballistic Mat Depot', 'Upon closer inspection, the mats appear to be some kind of armor plating.'
                 "These may be useful later. There is an exit to the east.", None, None, 'storage_corridor_s', None,
                 None, None, None, None, None, None)
dummy_depot = Room('Dummy Depot', 'As you walk in the room, one of the dummies reaches out, snapping and breaking from'
                   'being inflexible, grabbing for you. It speaks with a static rasp, crackling out "здесь '
                   "небезопасно уходите сейчас, which you somehow know to mean 'It is not safe here, leave now.' in "
                   'Russian. You now know it is not safe "here," wherever "here" may be, though you do not know the '
                   'reason. There is a door to the workshop to your north.', 'workshop', None, None, None, None, None,
                   None, None, None, None)
master_bed = Room('Master Bedroom', 'You are in a bedroom with a box of supplies on a shelf. You see them but do not '
                  'know for sure what they are for. They are all round, some are pointed and some are flat, and there '
                  'are others still that look like grenades, but less lethal and more cylindrical. They all have metal '
                  'ends. They all feel dangerous, but some seem like you need a bigger tool to use them. There is a '
                  'a laundry room to your northeast. A short corridor lies to your south.', None, 'f_2nd_corridor',
                  None, None, None, None, 'laundry_inner', 'bathroom', None, None)
basement_stair_in = Room('Basement Stairs', 'You are on a stair case that leads down to basement corridor and up to the'
                         ' first floor.', 'basement_corridor', None, None, None, None, None, None, None,
                         'main_stairs', None)
stairs_2nd = Room('Second Floor Stairs', 'You are on a flight of stairs that leads up to the third floor, and down to '
                  'the first floor. There is also a path north to a short hallway.', None, None, None, None, None, None,
                  None, None, 'stairs_3rd', 'main_stairs_1st')
stairs_3rd = Room('Third floor stairs', 'There is a bent corridor to your north and the second floor is below you.',
                  'storage_corridor_s', None, None, None, None, None, None, None, None, 'stairs_2nd')
storage = Room('Storage', 'You are in a room with lots of supplies for the base. There are so many things that could be'
               'of use to you it boggles you. There are a few guns, but you have a feeling there will be more in the '
               'boxes and crates lying around but from what you can see there is a SuperNova shotgun, a R4C assault'
               'rifle, and a Desert Eagle 50 caliber pistol. There are two metal crates that are unlocked. There is a '
               'door to your east.', None, None, 'storage_corridor_s', None, None, None, None, None, None, None)
workshop = Room('Workshop', 'There is a workbench and a boatload of tools you have never seen but somehow know how to '
                'use. There are enough tools and machines to craft very complex things, maybe even small firearms. '
                'There are doors to your north and west that lead into the storage corridor.', 'storage_corridor_e',
                None, None, 'storage_corridor_s', None, None, None, None, None, None)
piano_lounge = Room('Piano Lounge', 'There is a piano in the middle of the room. It appears to be in working order.'
                    'There is a dining room to your south and a long corridor to the west.', None, 'dining_room', None,
                    'main_corridor', None, None, None, None, None, None)
tv_room = Room('TV Room', 'There is a TV and a chair in front of it. The remote is on the chair. There is a door to the'
               'east.', None, None, 'main_corridor', None, None, None, None, None, None, None)
dining_room = Room('Dining Room', 'There is a dining table with a bunch of creepy mannequins around it. There are paths'
                   ' to your north to the piano room and west to the corridor.', 'piano_room', None, None,
                   'main_corridor', None, None, None, None, None, None)
garage = Room('Garage', 'As you enter the room, the feeling of "Man, I want out of here" hits you really hard. There is'
              ' a broken down car, and you realize that this is your ticket out of this place. There are most likely '
              'enough parts lying around the base to get this clunker working. There is a door into the hall to your '
              'west.', None, None, None, 'garage_corridor', None, None, None, None, None, None)
kitchen = Room('Kitchen', 'You are in a kitchen with lots of things appropriately suited to a kitchen. Frying pans, '
               'propane, and... gasoline, apparently. A few stoves look quite appealing to your tinkerer nature, and a '
               ' few parts from them may be useful. There are double doors to your east that lead to the long '
               'corridor and a door to your north that leads to the garage hall.' 'garage_corridor', None, None,
               'main_corridor', None, None, None, None, None, None, None)
maintenance = Room('Maintenance Area', 'You stand in a room with some cleaning solutions, a couple metal barrels, and a'
                   'bunch of mops. Ideas form in your creative head and you think, "Hey, maybe I can build a '
                   'mop-cannon!" There are doors to your east into the basement corridor and north into the armory.',
                   'armory', None, 'bm_corridor', None, None, None, None, None, None, None)
armory = Room('Armory', 'You have hit the motherlode of weaponry. Guns everywhere, and ammo everywhere else. All kinds '
              'of guns you recognize, and even more you have never seen before. SIX12 Modular shotgun, MK14 Marksman'
              'Rifle, M1A Carbine, Colt 1911 pistol, and a T-5 SMG, and all the ammo you could need. There are exits to'
              'the corridor on the northeast side of the room, and a path to the maintenance area at your south side.',
              None, 'maintenance', None, None, None, None, 'bm_corridor', None, None, None)
lockers = Room('Basement Lockers', 'There are a few unlocked street lockers here. There is an open area that connects '
               'the lockers to the corridor to your southwest.', None, None, None, None, None, 'bm_corridor', None,
               None, None, None)
bm_corridor = Room('Basement Corridor', 'You are in a corridor with lots of rooms connected to it. The maintenance area'
                   ' is to your southwest, stairs to your south, the armory to your north, locker area to your '
                   'northeast, and the briefing room to your east.', 'armory', 'basement_stair_in', 'briefing_room',
                   None, None, 'maintenance', 'lockers', 'briefing_room', None, None)
office = Room('Office', 'You are in an office with some office supplies like paper and staplers. There is a computer. '
              'You may be able to learn valuable information about the place. There is an exit to the hallway to the '
              'east', None, None, 'corridor_2', None, None, None, None, None, None, None)
f_2nd_corridor = Room('Second Floor Corridor', 'You are in the second floor corridor and there are three paths. North '
                      'leads to the master bedroom and northwest into the office. To your south lies a flight of stairs'
                      'leading up and down.', 'master_bed', 'stairs_2nd', None, None, 'office', None, None, None, None,
                      None)


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
    def __init__(self, name, description, damage, size, blast_type, blast_size, blast_description):
        super(Weapon, self).__init__(name, description, damage, size)
        self.type = blast_type
        self.blast = blast_size
        self.pin = True
        self.spoon_dropped = False
        self.thrown = False
        self.blast_description = blast_description

    def pull_pin(self):
        print('You pull the pin on the grenade, but hold the spoon in place')
        self.pin = False

    def drop_spoon(self):
        if self.pin is False:
            print('You drop the spoon and the grenade will explode in 5 seconds')
        if self.pin is True:
            print('You cannot drop the spoon until you pull the pin')

    def detonate(self):
        print('The %s explodes and a %s ensues' % self.name, self.blast_description)

    def throw(self):
        print('You throw the grenade as far away from you as you can')
        self.thrown = True


class Flashbang(Grenade):  # blast description = a blinding white light and a loud bang
    def __init__(self, name, description, damage, size, stun_time):
        super(Grenade, self).__init__(name, description, damage, size)
        self.stun = stun_time


class Frag(Grenade):  # blast description = a storm of shrapnel and a boom
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
        super(Rifle, self).__init__(name, description, 39, size)


class SuperNova(Shotgun):  # 48 damage, shotty* round
    def __init__(self, name, description, damage, size):
        super(Shotgun, self).__init__(name, description, 48, size)
        self.mag = 'set of shells'

    def fire(self):
        print('You pull the trigger and the end of your %s explodes in a glorious, deadly flame, and you rack the pump'
              '' % self.name)

    def reload(self):
        print('You slam a fresh set of shells into the %s' % self.name)


class D50(Pistol):  # 71 damage, pistol round
    def __init__(self, name, description, damage, size):
        super(Pistol, self).__init__(name, description, 71, size)


class SIX12(Shotgun):  # 45 damage, shotty* round
    def __init__(self, name, description, damage, size):
        super(Shotgun, self).__init__(name, description, 45, size)
        self.mag = 'drum'

    def reload(self):
        print('You slam a new drum into the %s' % self.name)


class MK14(Rifle):  # 60 damage, rifle round
    def __init__(self, name, description, damage, size):
        super(Rifle, self).__init__(name, description, 60, size)


class L85A2(Rifle):  # 47 damage, rifle round
    def __init__(self, name, description, damage, size):
        super(Rifle, self).__init__(name, description, 47, size)


class M1A1Carbine(Rifle):  # 40 damage, rifle round
    def __init__(self, name, description, damage, size):
        super(Rifle, self).__init__(name, description, 40, size)


class Colt1911(Pistol):  # 58 damage, pistol round
    def __init__(self, name, description, size):
        super(Pistol, self).__init__(name, description, 58, size)


class T5smg(SMG):  # 30 damage, pistol round
    def __init__(self, name, description, size):
        super(SMG, self).__init__(name, description, 30, size)


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


class Character(object):
    def __init__(self, name, description, health, dialogue, status_effect, inventory, target,
                 weapon=Weapon("Hands", "Your fists", 10, 1)):
        self.name = name
        self.description = description
        self.health = health
        self.life = True
        self.dialogue = dialogue
        self.status_effect = status_effect
        self.inventory = inventory
        self.target = target
        self.weapon = weapon

    def injure(self, damage):
        self.health -= damage
        print('%s is hurt and loses %s health' % self.name, damage)

    def attack(self, target):
        hit_chance = random.randint(1, 100)
        if hit_chance >= 50:
            target.injure(self.weapon.damage)

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

    def suicide_bomb(self):
        print('As the bomber runs towards you, he presses a detonator and blows his bomb vest up')
        self.health -= 290


current_node = spawn
miscCommands = ['yeet', 'jump', 'shout', 'cry', 'yell']
directions = ['north', 'south', 'east', 'west', 'northwest', 'southwest', 'northeast', 'southeast']
short_directions = ['n', 's', 'e', 'w', 'nw', 'sw', 'ne', 'se']
suicide = 'kill self'
while True:
    print(current_node.name)  # self.name(?)
    print(current_node.description)  # self.description(?)
    command = input('>_').lower().strip()
    if command in short_directions:
        pos = short_directions.index(command)
        command = directions[pos]
    if command in directions:
        try:
            current_node.move(command)
        except KeyError:
            print("That's a wall. Those are typically solid and not a lot of things your size can pass through those.")
    elif command == 'YEET':
        print('This b**** is empty! YEET!!')
    elif command == 'JUMP':
        print('*jumping intensifies*')
    elif command in ['SHOUT', 'YELL']:
        print('ARRRGGHHHH!!!')
    elif command == 'CRY':
        print('Boo hoo!')
    elif command == suicide:
        print('Is that really how you want to go out? By just taking your own life?')
        if command == 'YES':
            print('Well, alright then. You plunge your knife into your chest, and as you feel your blood slowly running'
                  'out, your world slowly blackens into nothingness.')
        if command == 'NO':
            print('Thank you for making the right choice. If you ever feel like giving up, remember to talk to someone'
                  ' who is a professional counselor.')

    else:
        print('I do not recognize that command.')
    if command == 'quit':
        quit(0)
