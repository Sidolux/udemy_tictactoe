from sys import exit


def player_marker(tekst=''):
    '''
    Returns selected Tic Tac Toe mark. Checks if input is o or x (CI)

    '''

    char = ''
    select = ''
    while select.lower() not in ('x', 'o'):
        select = input(tekst + ' ')
        if select.lower() == 'quit':
            exit(0)
    return select.lower()


def display_board(board):
    print(f'{board[7]}|{board[8]}|{board[9]}')
    print(f'-----')
    print(f'{board[4]}|{board[5]}|{board[6]}')
    print(f'-----')
    print(f'{board[1]}|{board[2]}|{board[3]}')


def place_marker(board, marker, position):
    board[position] = marker


def player_position(tekst=''):
    position = None
    while position not in range(1, 10):
        usr_input = input(tekst)
        try:
            position = int(usr_input)  # get player input
        except:
            if str(usr_input).lower() == 'quit':
                exit(0)
            print('To nie jest liczba')
            continue
        if position not in range(1, 10):
            print('Podaj liczbę z zakresu 1-9')
    return position


def check_win(board, marker):
    win_conditions = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7))
    for win_cond in win_conditions:
        win_set = set()
        for win_pos in win_cond:
#            print(str(win_pos)+board[win_pos], end='')
            win_set.add(board[win_pos])
#        print('')
#        print(win_cond, win_set, len(win_set), marker)
        if len(win_set)==1 and marker in win_set:
            return True
    return False

    #if len(win_set) == 1 and win_set[0]==marker:
    #    return True
    #else:
    #    return False


