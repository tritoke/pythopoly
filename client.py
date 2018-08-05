import socket
from Pythopoly import *

# IP = "192.168.0.192" # school
IP = "192.168.23.1"  # home
# AF_INET means an ipv4 address
# SOCK_STREAM means a tcp connection


print("hello and welcome to pythopoly by Sam Leonard")
print("please enter your name below")
user_name = input()


def join_game():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((IP, PORTNUM))
    client_socket.send(bytes(user_name, data_encoding))
    data = client_socket.recv(1024)
    print(data.decode(data_encoding))
    client_socket.close()


def get_state():
    turn_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    turn_socket.bind((IP, PORTNUM))
    turn_socket.listen(1)
    while True:
        connection, address = turn_socket.accept()
        received = connection.recv(1024)

        if len(received) > 0:
            recv_data = received.decode(data_encoding)
            state = recv_data.split("_")[0]
            print(state)
            if state == "board":
                draw_board(recv_data.split("_")[1::])
            elif state == send_options[0]:
                choice = display_options()
                connection.send(bytes(turn_choices[choice], data_encoding))
            connection.close()
            break

    turn_socket.close()

    return False


join_game()
Bankrupt = False
while not Bankrupt:
    Bankrupt = get_state()
