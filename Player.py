board_length = 38


class Player:
    name = None
    board_position = 0
    player_id = None  # make this a large random key known only to the server
    ip_address = None
    properties = []

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

    def update_board_position(self, places):
        self.board_position = (self.board_position + places) % board_length

    def get_properties(self):
        return self.properties

    def set_properties(self, properties):
        self.properties = properties
