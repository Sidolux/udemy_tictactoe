from os import system
# from sys import exit
from functions import *

restart = True
# Game restart loop
while restart:
    # setting variables
    xo = ['O', 'X']
    board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    who = 0
    pos = 0
    system('cls')
    # display splash screen
    print('''
-------------------------
| Gra w kółko i krzyżyk |
-------------------------

Kieruj się komunikatami.
Pola na planszy są ponumerowane jak na klawiaturze numerycznej komputera.

Powodzenia.

    ''')
    # ask for players
    player1_name = input('Podaj imię gracza 1: ')
    player2_name = input('Podaj imię gracza 2: ')

    xo_select = player_marker(player1_name + ' wybiera czym gra (O/X)')

    if xo_select.lower() == 'x':
        players = [player2_name, player1_name]
    else:
        players = [player1_name, player2_name]
    print(f'\nZaczyna O, dlatego pierwszy gra gracz {players[0]}')
    input('\nNaciśnij enter')
    system('cls')
    print('')
    display_board(board)
    print('')
    # main game loop
    while True:
        # ask for position and check if place is available
        while board[pos] in ('X', 'O', '#'):
            pos = player_position(players[who] + ', gdzie postawić ' + xo[who] + ' (1-9)')
            if board[pos] != ' ':
                print('Pole zajęte, wybierz inne pole.')
        # put marker on selected position
        place_marker(board, xo[who], pos)
        system('cls')
        print('')
        display_board(board)
        print('')
        # check if player won, or board full (tie)
        won = check_win(board, xo[who])
        if won or ' ' not in set(board):
            # won message
            if won:
                print(f'BRAWO {players[who]}!!! ZWYCIĘSTWO.')
            # tie message
            else:
                print('REMIS')
            # ask if replay
            player_continue = ''
            while player_continue not in ('t', 'n'):
                player_continue = input('\nGramy jeszcze raz T/N? ').lower()
            if player_continue == 'n':
                restart = False
            break
        who = (who + 1) % 2
print('\nDziękuję za grę!')
