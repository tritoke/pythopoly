from random import randint

corner_positions = [0, 9, 19, 28]
# these are the positions of the corners
long_name_positions = [11, 16, 31, 34, 36]
# these are all of the positions on the sides of the board which have name longer than length 2
sides = [10, 12, 13, 14, 15, 17, 18, 29, 30, 32, 33, 35, 37]
# these are all of the positions on the side of the board
board_dict = {0: "0", 1: "!", 2: "?", 3: "$", 4: "%", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "a", 11: "b", 12: "c",
              13: "d", 14: "e", 15: "f", 16: "g", 17: "h", 18: "i", 19: "j", 20: "k", 21: "l", 22: "m", 23: "n",
              24: "o", 25: "p", 26: "q", 27: "r", 28: "s", 29: "t", 30: "u", 31: "v", 32: "w", 33: "x", 34: "y",
              35: "z", 36: "#", 37: "~"}


def roll_dice():
    roll_one = randint(1, 6)
    roll_two = randint(1, 6)
    return roll_one + roll_two, roll_one == roll_two


def generate_board(players):
    board_list = [""]*38
    # this generates a list of length 38, filled with zeros
    for player in players:
        player_position = player.get_board_position()
        player_id = player.get_player_id()
        board_list[player_position] += f"P{player_id}"
    return board_list


def draw_board(board_positions):
    with open("board") as board:
        out = board.read()
        for i in range(len(board_positions)):
            if i in corner_positions:
                x = 4 - (len(board_positions[i])//2)
            elif i in sides:
                x = 3 - (len(board_positions[i])//2)
            else:
                x = 2 - (len(board_positions[i])//2)
            buffer = " " * x
            replace = f"{buffer}{board_positions[i]}{buffer}"
            out = out.replace(board_dict[i], replace)
    print(out)