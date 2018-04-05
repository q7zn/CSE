class Room(object):
    def __init__(self, name, north):
        self.name = name
        self.north = north

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


hdum = Room()

current_node = hdum
miscCommands = ['YEET', 'JUMP', 'SHOUT', 'CRY', 'YELL']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'NORTHWEST', 'SOUTHWEST', ' NORTHEAST', 'SOUTHEAST']
suicide = 'KILL SELF'
while True:
    print(current_node['NAME'])  # change
    print(current_node['DESCRIPTION'])  # change
    command = input('>_')
    if command in directions:
        try:
            # change
            name_of_node = current_node['PATHS'][command]
            current_node = hereford_map[name_of_node]
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
