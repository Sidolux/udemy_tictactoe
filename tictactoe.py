from os import system
from sys import exit
from functions import *


xo = ['O', 'X']
board = [' ','1','2','3','4','5','6','7','8','9']
print(board)
who=0
system('cls')
print('Gra Tic Tac Toe')
player1_name = input('Podaj imię gracza 1: ')
player2_name = input('Podaj imię gracza 2: ')

xo_select = player_input(player1_name + ' wybiera czym gra (O/X)')

if xo_select.lower() == 'x':
    players = [player2_name, player1_name]
else:
    players = [player1_name, player2_name]

print(f'Zaczyna O, dlatego pierwszy gra gracz {players[0]}')
input('Naciśnij enter')
system('cls')
print('')
print(f'{board[7]}|{board[8]}|{board[9]}')
print(f'-----')
print(f'{board[4]}|{board[5]}|{board[6]}')
print(f'-----')
print(f'{board[1]}|{board[2]}|{board[3]}')
print('')
print(f'{players[who]}, gdzie postawić {xo[who]} (1-9)')
