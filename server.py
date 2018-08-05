from Player import Player
from json import load
from random import randint
from Pythopoly import *
import socket

# IP = "192.168.0.192" # school
IP = "192.168.23.1"  # home
players = []


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
    server_socket.bind((IP, PORTNUM))
    server_socket.listen(10)
    print(f"listening on port: {PORTNUM}")

    joined_players = 1

    # this while loop runs until all players have joined
    while joined_players < num_players:
        connection, address = server_socket.accept()
        print(address[0])
        received = connection.recv(1024)
        if len(received) > 0:
            joined_players += 1
            new_player_name = received.decode(data_encoding)
            players.append(Player(name=new_player_name, ip_address=address[0], player_id=joined_players))
            data = bytes(f"Hello and welcome to pythopoly.\n"
                         f"{new_player_name} you are player: P{joined_players}",
                         data_encoding)
            connection.send(data)
        connection.close()
    server_socket.close()


def send_to_all(*, players, data, type):  # appends the packet type to the start then the rest is data
    if type == "board":
        prepend_str = type + "_"
        byte_data = bytes(prepend_str + "_".join(data), data_encoding)
        for player in players:
            if player.get_ip_address() == "HOST":
                draw_board(data)
            else:
                board_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                board_socket.connect((player.get_ip_address(), PORTNUM))
                board_socket.send(byte_data)
                board_socket.close()
    else:
        print("\n\n\n\n\nUNKNOWN TYPE PARAMETER IN SEND_TO_ALL\n\n\n\n")


def send_to_player(*, player, type):
    player_ip = player.get_ip_address()
    if player_ip == "HOST":
        return display_options()
    else:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print((player_ip, PORTNUM))
        client_socket.connect((player_ip, PORTNUM))
        client_socket.send(bytes(send_options[type], data_encoding))
        recv_data = client_socket.recv(1024)
        received = recv_data.decode(data_encoding)
        client_socket.close()
        return received


# def pickup_card(type, player):
#     with open(type + ".json") as file:
#         cards = load(file)["cards"]
#         card = cards[randint(0, len(cards))]
#         if card["affects"] == "player":
#             for action in card["actions"]:
#                 exec("player" + action)
#         else:
#             for i in players:
#                 if i != player:
#                     exec("i" + card["actions"][0])
#                 else:
#                     exec("player" + card["actions"][1])


# def check_bankrupt(players):
#     for player in players:
#         if player.get_money() < 0:
#             if player.get_net_worth() < 0:
#             # TODO this entire thing about bankrupcy
#             else:
#         # TODO allow the bankrupt player to liquidate assets to stay afloat


def main():
    start_game()
    while len(players) > 1:
        send_to_all(players=players, data=generate_board(players), type="board")
        for player in players:
            action = send_to_player(player=player, type=0) # their turn
            if action == "move":
                spaces = roll_dice()
                print(f"moving {spaces}")
                player.move(spaces)
    # players.append(Player(name="Sam", ip_address="HOST", player_id=1))
    # things = players[0].get_properties()
    # print(things)
    # print(things["property_ids"])
    # print(things["num_houses"])
    # check_bankrupt(players)
    # start_game()
    # board_positions = generate_board(players)
    # send_to_all(player_list=players, data=board_positions, type="board")
    # current_player = randint(0, len(players))


main()
