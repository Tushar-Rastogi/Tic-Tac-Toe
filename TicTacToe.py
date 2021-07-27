the_board = {}
HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
GREEN = '\033[92m'
Yellow = '\033[93m'
RED = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'


def check_game_end(board):
    end = False
    if board['1'] == board['2'] == board['3']:
        end = True
    elif board['4'] == board['5'] == board['6']:
        end = True
    elif board['7'] == board['8'] == board['9']:
        end = True
    elif board['1'] == board['4'] == board['7']:
        end = True
    elif board['2'] == board['5'] == board['8']:
        end = True
    elif board['3'] == board['6'] == board['9']:
        end = True
    elif board['1'] == board['5'] == board['9']:
        end = True
    elif board['3'] == board['5'] == board['7']:
        end = True
    return end


def printBoard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('---+---+---')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('---+---+---')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])


def get_position(side):
    valid = range(1, 10)
    index = 0
    while index not in valid:
        index_str = input(f"Enter number (1-9) where you want to input '{side}': ")
        if index_str.isdigit():
            index = int(index_str)
            if index in valid:
                pass
            else:
                print("Value not is defined range (1-9)!!!")
        else:
            print("Your input is not valid!!!")
    return index


def get_player_one_side(player_one_name):
    valid = ['o', 'x']
    side = 'start'
    while side not in valid:
        side = input(f"{player_one_name} choose your side (x or o): ")
        if side in valid:
            pass
        else:
            print("Not valid input, choose x or o!!!")
    return side


def update_board(index, value):
    if value == 'x':
        string = ' ' + HEADER + BOLD + value + ENDC + ' '
    else:
        string = ' ' + GREEN + BOLD + value + ENDC + ' '
    the_board[str(index)] = string
    printBoard(the_board)


def play_again_method(play_again):
    while play_again not in ('y', 'n'):
        play_again = input('Do you want to play again? y or n: ')
        if play_again not in ('n', 'y'):
            print('Not valid answer please select y for \'YES\' or n for \'NO\'')
        else:
            return play_again


def run_game():
    print()
    # display_initial_board(" <1> | <2> | <3> ", " <4> | <5> | <6> ", " <7> | <8> | <9> ")
    print("Let's play Tic-Tac-Toe!!!")
    player_one_name = input("Enter player 1 name: ")
    player_two_name = input("Enter player 2 name: ")
    player_one = get_player_one_side(player_one_name)
    player_two = ''
    if player_one == 'x':
        side = {'x': player_one_name, 'o': player_two_name}
    else:
        side = {'o': player_one_name, 'x': player_two_name}
    printBoard(the_board)
    turn = player_one
    free_indexes = list(range(1, 10))

    # Start Game two players
    for _ in range(9):
        print()
        print('{} your chance'.format(side[turn]))
        index = get_position(turn)
        import os
        size = os.get_terminal_size()
        print('\n' * (size.lines - 9))
        while index not in free_indexes:
            import os
            size = os.get_terminal_size()
            print('\n' * size.lines)
            print("You have selected already taken index!!!")
            print("Select from these indexes : " + str(free_indexes))
            index = get_position(turn)
            print('\n' * (size.lines - 9))
        update_board(index, turn)
        if check_game_end(the_board):
            print(f'{side[turn]} WON!!!')
            play_again = 'No'
            return play_again_method(play_again)
        if turn == 'x':
            turn = 'o'
        else:
            turn = 'x'
        free_indexes.remove(index)
        if len(free_indexes) == 0:
            print("Match DRAW!!!")
            play_again = 'No'
            return play_again_method(play_again)


def run_with_computer():
    print("Let's play Tic-Tac-Toe!!!")
    player_name = 'You'
    player_two = 'Computer'


if __name__ == '__main__':
    import psutil
    import os

    pid = os.getppid()  # Get parent process id
    print()
    if psutil.Process(pid).name() not in ['zsh', 'bash']:
        print(RED + "Run this script from TERMINAL/COMMAND PROMPT!!!" + ENDC)
        quit()

    play = 'y'
    while play == 'y':
        the_board = {
            '1': ' 1 ', '2': ' 2 ', '3': ' 3 ',
            '4': ' 4 ', '5': ' 5 ', '6': ' 6 ',
            '7': ' 7 ', '8': ' 8 ', '9': ' 9 '
        }
        mode = ''
        while mode not in ('S', 'D', 's', 'd'):
            mode = input('(S)ingle or (D)ouble: ')
            if mode not in ('S', 'D', 's', 'd'):
                print('Please select s or d!!!')
        if mode in ('D', 'd'):
            play = run_game()
        else:
            play = run_with_computer()
    print("Tnx for playing!!")
