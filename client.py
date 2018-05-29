import socket
import Pythopoly

# ICT 4-02
# 192.168.0.192 me
# 192.168.0.90 ian

PORTNUM = 9987
location = "home"
# location indicates whether I am at home or at school and change the IP accordingly
IP = {"school": "192.168.0.192", "home": "192.168.23.1"}
# AF_INET means an ipv4 address
# SOCK_STREAM means a tcp connection


print("hello and welcome to pythopoly by Sam Leonard")
print("please enter your name below")
user_name = input()


def join_game():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((IP[location], PORTNUM))
    client_socket.send(bytes(user_name, "utf-8"))
    data = client_socket.recv(1024)
    print(data.decode("utf-8"))
    client_socket.close()


def get_board():
    board_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    board_socket.bind((IP[location], PORTNUM))
    board_socket.listen(10)
    while True:
        connection, address = board_socket.accept()
        print(address)
        received = connection.recv(1024)
        if len(received) > 0:
            board_positions = received.decode("utf-8").split("_")
            Pythopoly.draw_board(board_positions)
        connection.close()
        break
    board_socket.close()

def wait_turn():
    turn_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    turn_socket.bind((IP[location], PORTNUM))
    turn_socket.listen(10)
    turn = ""
    while True:
        connection, address = turn_socket.accept()
        print(address)
        received = connection.recv(1024)
        if turn == "True" and len(received) > 0:

        if len(received) > 0:
            turn = received.decode("utf-8")

        connection.close()
        if turn != "True":
            break
    turn_socket.close()
    if turn == "bankrupt":
        return True
    else:
        return False




join_game()
Bankrupt = False
while Bankrupt != True:
    get_board()
    Bankrupt = wait_turn()

