#Connect four, for learning purposes. By /u/A440251.

"""
Welcome to Connect Four!

Please input an answer:

An answer of "!STARTAI" will start a game against the computer.
An answer of "!START2P" will start a game for two players.
An answer of "!QUIT" will quit the game.

"""

def create_empty_board(): 
    return [[' ' for i in range(7)] for i in range(6)]

def draw_board(board):
    """
    Arg: Board representation as number string
    Ret: Prints the board out, returns nothing
    """
    board_counter = {}
    board_representation = create_empty_board()
    count = 0
    for letter in board:
        if count % 2 == 0:
            count += 1
            piece = 'x'
        elif count % 2 == 1:
            count += 1
            piece = 'o'
        if letter not in board_counter:
            board_counter[letter] = 1
            row_index = board_counter[letter] - 1
            column_index = int(letter) - 1
            board_representation[row_index][column_index] = piece
        else:
            row_index = board_counter[letter] - 1
            board_counter[letter] += 1
            board_representation[row_index][column_index] = piece

    print("Print board_representation:")
    print(board_representation)
    
    for i in range(6):
        print('|'.join(board_representation[5-i]))
    print("1 2 3 4 5 6 7")
    print("here it was!")

def board_counts(board):
    board_count = {}
    for letter in board:
        if letter not in board:
            board_count[letter] = 1
        else:
            board_count[letter] += 1
    return board_count

            
def START_AI():
    print("AI functionality is not in place yet.")

def START_2P():
    new_board = create_empty_board()
    #board as string representation
    board = ''
    p1_turn = True
    turn_number = 1
    draw_board(board)

    pass

def welcome():
    print(__doc__)

def game_over(board):
    """
    Arg: Board representation as number string
    Ret: True or false, based on if a player has connect four
    """
    if (False):
        pass
    else:
        return(False)

def legality_check(board, move):
    """
    Arg: Board representation as number string, move taken
    Ret: True or false, based on if the move is legal
    """
    count = board_counts(board)
    if count[move] <=5:
        return True
    else:
        return False

def main():
    done = False
    while not done:
        welcome()
        answer = input("What is your answer?\n...>")
        if answer.upper() == "!STARTAI":
            START_AI()
        if answer.upper() == "!START2P":
            START_2P()
        if answer.upper() == "!QUIT":
            print("Thanks for playing Connect Four. Goodbye!")
            break
        else:
            print("I didn't understand that. Please try again!")
        


def tests():
    empty_board = create_empty_board()
    test_board = '123615734132577'
    print("This should print an empty board:")
    print(empty_board)
    print("This uses the draw_board():")
    draw_board(test_board)

if __name__ == "__main__":
    tests()
    print("---END OF TESTS---")
    #main()
