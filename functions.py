from sys import exit


def player_input(tekst=''):
    '''
    Returns selected Tic Tac Toe mark

    '''

    char = ''
    select = ''
    while select.lower() not in ('x', 'o'):
        select = input(tekst + ' ')
        if select.lower() == 'quit':
            exit(0)
    return select.lower()
