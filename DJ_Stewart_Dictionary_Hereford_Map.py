
current_node = hereford_map['SPAWN']
miscCommands = ['YEET', 'JUMP', 'SHOUT', 'CRY', 'YELL']
hereford_map = {
    'SPAWN': {
        'NAME': 'Stair Alley',
        'DESCRIPTION': "You wake up and find yourself in an alley. There are two sets of stairs,\none to your "
                       "west that leads up and one to your northwest that leads down.",
        'PATHS': {
            'WEST': 'SIDESTAIR',
            'NORTHWEST': 'BASEMENTSTAIR'
        }
    },
    'SIDESTAIR': {
        'NAME': 'Side Staircase ',
        'DESCRIPTION': 'You are on a staircase with two flights that leads up to the second and third floor of a large '
                       'building. \nYou stand on the second floor platform with a door to your west. The third floor '
                       'door is to your south. There is an alley to your east.',
        'PATHS': {
            'WEST': 'LAUNDRYROOM',
            'EAST': 'SPAWN',
            'SOUTH': 'STORAGECORRIDOR'  # need
        }
    },
    'BASEMENTSTAIR': {
        'NAME': 'Basement Stair Entrance',
        'DESCRIPTION': 'You are on a staircase and there is a path that looks from your angle to be a dead end to your '
                       'south, though it may be worth checking out. There are stairs to your east and west.',
        'PATHS': {
            'WEST': 'SPAWN',
            'EAST': 'FRONTACCESS',  # need
            'SOUTH': 'BASEMENTENTRANCE'
        }
    },
    'FRONTACCESS': {
        'NAME': "Front Access",
        'DESCRIPTION': 'A door wide enough for two people to enter side by side stands to your south. There is a set of'
                       ' stairs leading down to your east.',
        'PATHS': 'BASEMENTSTAIR'
    },
    'BASEMENTENTRANCE': {
        'NAME': 'Basement Entrance',
        'DESCRIPTION': 'You find yourself in what looked before like a dead end, but there is a door to your west that '
                       'must lead to the basement. There are staircases to your north.',
        'PATHS': {
            'NORTH': 'BASEMENTSTAIR',
            'WEST': 'BRIEFROOM'
        }
    },
    'LAUNDRYROOM': {
        'NAME': 'Laundry Room',
        'DESCRIPTION': 'You are in a room with a wall directly in front of you that spans almost the whole way to the'
                       'wall to your south. \nThere is an opening, however, to your southwest end of the extended wall.'
                       ' There is a door to your east. There are many washing machines and related '
                       '\nappliances in the room. They might have something in them.',
        'PATHS': {
            'SOUTHWEST': 'LAUNDRYROOM.INNER',
            'EAST': "SIDESTAIR"

        }
     },

}
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'NORTHWEST', 'SOUTHWEST', ' NORTHEAST', 'SOUTHEAST']
suicide = 'KILL SELF'
while True:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input('>_')
    if command in directions:
        try:
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
