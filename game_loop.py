room_dict = {
    'start': {'id': 1, 'name': 'main room', 'width': 3, 'depth': 3, 'height': 1, 'desc': 'dimly lit'},
    'library': {'id': 2, 'name': 'library', 'width': 3, 'depth': 3, 'height': 1, 'desc': "mr pippin's library"},
    'study': {'id': 3, 'name': 'study', 'width': 2, 'depth': 2, 'height': 1, 'desc': "the chemist's study"},
}


class room:
    def __init__(self, name):
        self.room = room_dict[name]

    def get_room_name(self):
        return self.room['name']

    def get_room_desc(self):
        return self.room['desc']

    def __str__(self):
        return self.room['name']


class location:
    def __init__(self, room, x, y):
        self.room = room
        self.x = x
        self.y = y

    def get_desc(self):
        return 'room %s %s x %s  y %s' % (self.room.get_room_name(), self.room.get_room_desc(), self.x, self.y)


class weapon:
    weapon_dict = {
        'club': {'speed': 3, 'damage': 5},
        'spiney throwing star': {'speed': 9, 'damage': 2}
    }

    def __init__(self, name):
        self.weapon = self.weapon_dict[name]


inhabitant_dict = {
    'gnome': {'name': 'gnar', 'strength': 7, 'defense': 7, 'description': 'toothy gnar gnar',
              'location': location(room('start'), 2, 3)},
    'player': {'name': 'snoop dog', 'strength': 7, 'defense': 7, 'description': 'supa sly',
               'location': location(room('start'), 2, 1)}
}


class inhab:
    # def get_context(self):
    #     desc_string = 'you are %s, %s - in %s postion %s %s' % (self.inhab['name'], self.inhab['description'] , self.inhab['location'][0],self.inhab['location'][1],self.inhab['location'][2])


    # return desc_string

    def __init__(self, name):
        self.inhab = inhabitant_dict[name]

    def get_name(self):
        return self.inhab['name']

    def get_location(self):
        return self.inhab['location']

    def get_desc(self):
        return self.inhab['description']

    def __str__(self):
        return str(self.inhab)

    def get_move(self):
        return raw_input('what is your move?\n')

    def get_available_moves(self):
        return 'forward, back, left, right, strike'

    def do_move(self, command):
        if command == 'forward':
            # find location, move one step forward, save
            l = self.inhab['location']
            print 'you are in room %s position %s %s' % l
            print 'move'
            self.inhab['location'] = (l[0], l[1], l[2] + 1)
        if command == 'help':
            print self.get_available_moves()


class game_world:

    def get_proximity_desc(self, location):
        # search inhab table see if any thing close to location
        for i in inhabitant_dict:
            print inhabitant_dict[i]['location']


    def get_player_context(self, player):
        location_string = 'you are %s, %s - in %s' % (
        player.get_name(), player.get_desc(), player.get_location().get_desc())

        proximity_desc = get_proximity_desc(player.get_location())
        return desc_string

    def __init__(self, id, name):
        self.id = id
        self.name = name
        print 'creating world %s' % self.name

    def initialize(self):
        print 'initializing world'

        # initialize rooms
        self.the_world = {}
        self.the_world['rooms'] = [room('start'), room('library')]

        # initialize characters
        self.the_world['inhabitants'] = [inhab('gnome')]

    def get_player(self):
        return inhab('player')


if __name__ == "__main__":
    world = game_world(1, 'bad ass world 1')
    world.initialize()

    while True:
        player = world.get_player()
        print world.get_player_context(player)
        move = player.get_move()
        player.do_move(move)

        # world.step_time()
