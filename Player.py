import Pythopoly


class Player:
    name = None
    # board_position = 40 is in jail
    board_position = 0
    player_id = None  # make this a large random key known only to the server
    ip_address = None
    get_out_of_jail = 0
    jail_count = 0
    money = 25000
    properties = []
    num_properties = {"houses": 0, "hotels": 0}

    def __init__(self, *, name, player_id, ip_address):
        self.name = name
        self.player_id = player_id
        self.ip_address = ip_address

    def get_name(self):
        return self.name

    def get_player_id(self):
        return self.player_id

    def get_board_position(self):
        return self.board_position

    def get_ip_address(self):
        return self.ip_address

    def move(self, places):
        if self.board_position + places > Pythopoly.board_length:
            self.money += 2000
        self.board_position = (self.board_position + places) % Pythopoly.board_length

    def move_to(self, type):
        places = {"airports": [5, 15, 25, 35], "services": [12, 28], "stanstead": [15], "canary": [14], "docks": [24]}
        for i in places[type]:
            if i > self.board_position:
                self.board_position = i
                return
        self.board_position = places[type][0]
        self.money += 2000

    def set_board_position(self, position):
        self.board_position = position

    def get_properties(self):
        return self.properties

    def set_properties(self, properties):
        self.properties = properties

    def get_money(self):
        return self.money

    def set_money(self, increase):
        self.money += increase

    def get_num_properties(self, *, type):
        return self.num_properties[type]

    def set_num_properties(self, *, houses, hotels):
        self.num_properties["houses"] += houses
        self.num_properties["hotels"] += hotels

    def set_GOOJ(self, num):
        self.get_out_of_jail += num

    def get_GOOJ(self):
        return self.get_out_of_jail
