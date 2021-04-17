
import random


def cheack_board(board):
    new_board = []
    for i in range(len(board)):
        if board[i] == " ":
            new_board.append(i)
    return new_board


def choose_turn():
    dice = random.randint(1, 2)
    if dice == 1:
        player = '×'
        bot = 'o'
        print('Ты играешь за крестик')
        print(' ')
    else:
        player = 'o'
        bot = '×'
        print('Ты играешь за нолик')
        print(' ')
    return player, bot


def move_player(board, player, ):
    turn = int(input('Введите номер ячейки >>> '))
    new_board = cheack_board(board)  # 1 4 6

    while turn not in new_board:
        turn = int(input('Введите номер ячейки >>> '))
    board[turn] = player


def create_board():
    board = []
    for i in range(9):
        board.append(' ')
    return board


def display_board(board):
    print(board[0], "|", board[1], "|", board[2], )
    print("----------")
    print(board[3], "|", board[4], "|", board[5])
    print("----------")
    print(board[6], "|", board[7], "|", board[8])
    print()

def bot_move(board, bot):
    best_moves = [4, 0, 2, 6, 8, 1, 3, 5, 7]
    ways_2_win = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for best_move in best_moves:
        for way in ways_2_win:
            if best_move in way:
                x_1 = way[0]
                x_2 = way[1]
                x_3 = way[2]
                if (board[x_1] == ' ' or board[x_1] == bot)\
                        and (board[x_2] == ' ' or board[x_2] == bot) and \
                        (board[x_3] == ' ' or board[x_3] == bot):
                    if board[x_1] == ' ':
                        board[x_1] = bot
                        return
                    elif board[x_2] == ' ':
                        board[x_2] = bot
                        return
                    elif board[x_3] == ' ':
                        board[x_3] = bot
                        return


def change_turn(cur_turn):
    if cur_turn == "×":
        cur_turn = "o"
    else:
        cur_turn = "×"
    return cur_turn

def check_winner(board, player, bot):
    ways_2_win = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]
    for way in ways_2_win:
        x_1 = board[way[0]]
        x_2 = board[way[1]]
        x_3 = board[way[2]]
        if x_1 == x_2 == x_3 == player:
            print("Победил игрок")
            exit()
        elif x_1 == x_2 == x_3 == bot:
            print("Победил бот")
            exit()


def start():
    player, bot = "×", "o"
    board = create_board()
    cur_turn = '×'
    display_board(board)
    while True:
        if player == cur_turn:
            move_player(board, player)

        if bot == cur_turn:
            bot_move(board, bot)

        display_board(board)
        check_winner(board, player, bot)
        cur_turn = change_turn(cur_turn)


start()
