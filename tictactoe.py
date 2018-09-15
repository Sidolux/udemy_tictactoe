from os import system
from sys import exit
from functions import *

restart = True
while restart:
    xo = ['O', 'X']
    board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    who = 0
    pos = 0

    system('cls')
    print('Gra Tic Tac Toe')
    player1_name = input('Podaj imię gracza 1: ')
    player2_name = input('Podaj imię gracza 2: ')

    xo_select = player_marker(player1_name + ' wybiera czym gra (O/X)')

    if xo_select.lower() == 'x':
        players = [player2_name, player1_name]
    else:
        players = [player1_name, player2_name]

    print(f'Zaczyna O, dlatego pierwszy gra gracz {players[0]}')
    input('Naciśnij enter')
    system('cls')
    print('')
    display_board(board)
    print('')
    while True:
        while board[pos] in ('X', 'O', '#'):
            pos = player_position(players[who] + ', gdzie postawić ' + xo[who] + ' (1-9)')
            if board[pos] != ' ':
                print('Pole zajęte, wybierz inne pole.')
        place_marker(board, xo[who], pos)
        system('cls')
        print('')
        display_board(board)
        print('')
#        print(check_win(board, xo[who]))
        won = check_win(board, xo[who])
        if won or ' ' not in set(board):
            if won:
                print(f'BRAWO {players[who]}!!! ZWYCIĘSTWO.')
            else:
                print('REMIS')
            player_continue = ''
            while player_continue not in ('t', 'n'):
                player_continue = input('Gramy jeszcze raz T/N? ').lower()
            if player_continue == 'n':
                restart = False
            break
        who = (who + 1) % 2
print('\nDziękuję za grę.')
