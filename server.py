from Player import Player
from json import load
from random import randint
import Pythopoly
import socket

# home ip: 192.168.23.1
# school ip: 192.168.0.192

location = "home"
# location indicates whether I am at home or at school and change the IP accordingly
IP = {"school": "192.168.0.192", "home": "192.168.23.1"}
board_length = 38
players = []


# this dictionary stores the characters which represent each position in the board file


def start_game():
    print("hello and welcome to pythopoly, you are the host of this game.")
    print("please enter your name below")
    host_name = input()
    players.append(Player(name=host_name, player_id=1, ip_address="HOST"))

    print("please enter the number of players your game will have below")
    num_players = int(input())
    while num_players > 4 or num_players < 2:
        print("you can only have between 2 and four players")
        print("please enter the number of players your game will have below")
        num_players = int(input())

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((IP[location], Pythopoly.PORTNUM))
    server_socket.listen(10)
    print(f"listening on port: {PORTNUM}")

    joined_players = 1

    # this while loop runs until all players have joined
    while joined_players < num_players:
        connection, address = server_socket.accept()
        print(address)
        received = connection.recv(1024)
        if len(received) > 0:
            joined_players += 1
            new_player_name = received.decode("utf-8")
            players.append(Player(name=new_player_name, ip_address=address, player_id=joined_players))
            data = bytes(f"Hello and welcome to pythopoly.\n"
                         f"{new_player_name} you are player: P{joined_players}",
                         "utf-8")
            connection.send(data)
        connection.close()
    server_socket.close()


def send_to_all(*, player_list, data, type):
    if type == "board":
        data = bytes("_".join(data), "utf-8")
        for player in player_list:
            if player.ip_address == "HOST":
                Pythopoly.draw_board(data)
            else:
                board_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                board_socket.connect((player.ip_address[0], Pythopoly.PORTNUM))
                board_socket.send(data)
    else:
        print("man you gotta get round to this")

def send_to_player(player):
    player.get_ip_address()


def pickup_card(type, player):
    with open(type + ".json") as file:
        cards = load(file)["cards"]
        card = cards[randint(0, len(cards))]
        if card["affects"] == "player":
            for action in card["actions"]:
                exec("player" + action)
        else:
            for i in players:
                if i != player:
                    exec("i" + card["actions"][0])
                else:
                    exec("player" + card["actions"][1])

def check_bankrupt(players):
    for player in players:
        if player.get_money() < 0:
            if len(player.get_properties()) == 0:
                del players[player.get_player_id() -1]
            else:
                net_worth = player.get_money()
                for property in player.get_properties():
                    net_worth += Pythopoly.get_tile_data(property)["mortgage"] #TODO sort this mess out
                    if net_worth > 0:
                if net_worth < 0:





def main():
    start_game()
    board_positions = Pythopoly.generate_board(players)
    send_to_all(player_list=players, data=board_positions, type="board")
    current_player = randint(0, len(players))



main()
