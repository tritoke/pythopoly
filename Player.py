from random import randint
from json import load
import Pythopoly


class Player:
    name = None
    # board_position = 40 is in jail
    board_position = 0
    player_id = None  # make this a large random key known only to the server
    ip_address = None
    get_out_of_jail = 0
    money = 25000
    properties = []
    houses = 0
    hotels = 0

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

    # TODO sort out these methods and how they relate to the player

    # chooses a random card from community chest
    def community_chest(self):
        with open("community_chest.json") as file:
            cards = load(file)["cards"]
        card = cards[randint(0, len(cards))]
        for action in card["actions"]:
            exec("self." + action)
        #TODO setup sending of the message to the client / maybe make a method to do this

    @staticmethod
    # chooses a random chance card
    def chance():
        with open("chance") as file:
            cards = file.read().split("$")
        return cards[randint(0, len(cards))]

