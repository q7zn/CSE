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


spawn = Room('Stair Alley', 'You wake up and find yourself in an alley with no recollection of what happened or why you'
             ' are here. There are two sets of stairs,\none to your north that leads up and one to your northwest that '
             'leads down.', None, None, None, 'side_stair', 'basement_stair', None, None, None, None, None)
side_stair = Room('Side Staircase', 'You are on a staircase with two flights that leads up to the second and third '
                  'floor of a large building. \nYou stand on the second floor platform with  door to your west. The' 
                  'third floor door is to your south. There is an alley to your east.', None, 'storage_corridor',
                  'spawn', 'laundry_room', 'basement_entrance', None, None, None, None, None)
basement_stair_out = Room('Basement Staircase', 'You are on a staircase and there is a path that looks from your angle '
                          'to be a dead end to your south, though it may be worth checking out. There are stairs to '
                          'your east and west.', None, 'briefing_room', 'side_stair', 'front_access', None, None, None,
                          None, None, None)
briefing_room = Room('Briefing Room', 'You are in a room with a few projectors and some desks. There is a door leading '
                     'outside to your east, and there is a hallway to your west. One of the desks, the one to your '
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
                       'basement. There is a hallway to your north with lots of doors in it', 'main_corridor', None, None,
                       None, None, None, None, None, 'main_stairs_2nd', 'main_stairs_bm')
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
                          'the corner of the hall.', None, None, 'side_stair', None, None, None, None, None, None, None)
storage_corridor_n = Room('Storage Corridor Northeast', 'You are in the corner of the hallway. You can see down the '
                          'hall to the east and to the south. There is a room to your west with a bunch of things that '
                          'look like place mats. There is more hallway to your south.', None, 'storage_corridor_s',
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
                  'bathroom to your southeast and a laundry room to your northeast. A short corridor lies to your '
                  'south.', None, 'f_2nd_corridor', None, None, None, None, 'laundry_inner', 'bathroom', None, None)
basement_stair_in = Room('Basement Stairs', 'You are on a stair case that leads down to basement corridor and up to the'
                         ' first floor.', 'basement_corridor', None, None, None, None, None, None, None,
                         'main_stairs', None)
stairs_2nd = Room('Second Floor Stairs', 'You are on a flight of stairs that leads up to the third floor, and down to '
                  'the first floor. There is also a path north to a short hallway.', None, None, None, None, None, None,
                  None, None, 'stairs_3rd', 'main_stairs_1st')
stairs_3rd = Room('Third floor stairs', 'There is a bent corridor to your north and the second floor is below you.',
                  'storage_corridor_s', None,)
storage = Room()
workshop = Room()
piano_lounge = Room()
tv_room = Room()
dining_room = Room()
garage = Room()
kitchen = Room()
maintenance = Room()
armory = Room()
lockers = Room()
bm_corridor = Room()
f_1st_corridor = Room()
f_2nd_corridor = Room()
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
            print("That's a wall. Those are typically solid and not a lot of things your size can pass through.")
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
                  ' who professional counselor.')

    else:
        print('I do not recognize that command.')
    if command == 'quit':
        quit(0)