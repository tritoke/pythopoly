from Player import Player
import Pythopoly
import socket

# home ip: 192.168.23.1
# school ip: 192.168.0.192

PORTNUM = 9987
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
    server_socket.bind((IP[location], PORTNUM))
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


def send_board(*, player_list, board_positions):
    data = bytes("_".join(board_positions), "utf-8")
    for player in player_list:
        if player.ip_address == "HOST":
            Pythopoly.draw_board(board_positions)
        else:
            board_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            board_socket.connect((player.ip_address[0], PORTNUM))
            board_socket.send(data)



def main():
    # start_game()
    players.append(Player(name="Sam", player_id=1, ip_address="HOST"))
    # board_positions = Pythopoly.generate_board(players)
    # Pythopoly.draw_board(board_positions)
    # send_board(player_list=players, board_positions=board_positions)
    success = exec("players[0]." + Pythopoly.get_tile_data(2)["action"])



main()
