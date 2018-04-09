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


spawn = Room('Stair Alley', 'You wake up and find yourself in an alley. There are two sets of stairs,\none to your '
             'north that leads up and one to your northwest that leads down.', None, None, None, 'side_stair',
             'basement_stair', None, None, None, None, None)
side_stair = Room('Side Staircase', 'You are on a staircase with two flights that leads up to the second and third '
                  'floor of a large building. \nYou stand on the second floor platform with '
                  'a door to your west. The third floor door is to your south. There is an alley to '
                  'your east.', None, 'storage_corridor', 'spawn', 'laundry_room', 'basement_entrance', None, None,
                  None, None, None)
basement_stair = Room('Basement Staircase', 'You are on a staircase and there is a path that looks from your angle to '
                      'be a dead end to your south, though it may be worth checking out. There are stairs to your '
                      'east and west.', None, 'briefing_room', 'side_stair', 'front_access', None, None, None, None,
                      None, None)
briefing_room = Room('Briefing Room', 'You are in a room with a few projectors and some desks. There is a door leading '
                                      'outside to your east, and there is a hallway to your west. One of the desks, '
                                      'the one to your southwest, has a slightly open drawer.', 'basement_stair', None,
                                      'basement_stair', 'basement_corridor', None, 'brief_desk', None, 'brief_desk',
                                      None, None)
front_access = Room('Front Access', 'A door wide enough for two people to enter side by side stands to your south. '
                                    'There is a set of stairs leading down to your east.', None, 'main_corridor',
                                    'basement_stair', None, None, None, None, None, None, None)
main_corridor = Room('Main Corridor', 'You are in a long hallway with many rooms on both sides. There is an exit '
                                      'to the outside to your north, a kitchen to your south, and another hallway on '
                                      'your southwest. There is a room with some TVs in another room to your west, and '
                                      'a ')
brief_desk = Room()
laundry_room = Room()
laundry_inner = Room()
storage_corridor = Room()
mat_depot = Room()
dummy_depot = Room()
master_bed = Room()
main_stairs_bm = Room()
main_stairs_1st = Room()
main_stairs_2nd = Room()
main_stairs_3rd = Room()
storage = Room()
workshop = Room()
terrace = Room()
garage_corridor = Room()
piano_lounge = Room()
tv_room = Room()
dining_room = Room()
garage = Room()
kitchen = Room()
maintenance = Room()
armory = Room()
lockers = Room()
basement_corridor = Room()
f_1st_corridor = Room()
office = Room()
office_closet = Room()
kids_bed = Room()


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
            # change
            name_of_node = current_node['PATHS'][command]
            current_node = [name_of_node]
        except KeyError:
            print('Your legs are not programmed to go this way.')
    elif command == 'YEET':
        print('This thing is empty! YEET!!')
    elif command == 'JUMP':
        print('*jumping intensifies*')
    elif command in ['SHOUT', 'YELL']:
        print('ARRRGGHHHH!!!')
    elif command == 'CRY':
        print('Boo hoo!')
    elif command == suicide:
        print('Is that really how you want to go out? By just taking your own life?')
        if command == 'YES':
            print('Well, alright then. Your head spontaneously implodes and Lord Kek comes down to laugh at you. Even '
                  'the internet gods recognize your cowardice.')
        if command == 'NO':
            print('Thank you for making the right choice. If you ever feel like giving up, remember to talk to someone'
                  ' who professional counselor.')

    else:
        print('I do not recognize that command.')
    if command == 'quit':
        quit(0)
