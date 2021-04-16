#Importing required packages
import numpy as np

class Player:
    """
    This is a player class
    """
    def __init__(self, name, mark):
        self.name = str(name)
        self.mark = str(mark)

    def won(self):
        print(self.name,"won:)")

def get_board():
    """
    Getting the board
    """
    board = np.reshape(['-']*9, (3,3), order='C')
    return board

def play(p1, p2):

    """
    This function will start the game.
    """
    board = get_board()

    for turn in range(9):
        if(turn%2==0):
            player_plays(p1, board)
            if matched(p1, board):
                p1.won()
                game_end()
                return
        else:
           player_plays(p2, board)
           if matched(p2, board):
                p2.won()
                game_end()
                return
    #nine moves passed, so game is drawn
    print('Game Drawn')
    game_end()
    return

def place(mark, R, C, board):
    """
    This is to place the mark of player on the board
    """
    board[R][C] = mark

def verified(i, j, board):
    """
    This function will verify the position to place
    """
    if (i<3) and (j<3):
        return board[i][j]=='-'

def player_plays(player, board):
    """
    This function will complete the turn of a player
    """
    completed = False
    while not completed:
        print(f"{player.name}, your turn...")
        i,j = input('Enter RC with gap in b/w: ').split()
        i, j = int(i), int(j)
        if verified(i, j, board):
            completed = True
            place(player.mark, i, j, board)
            print_board(board)
        else:
            print(f"are you noob, {player.name}:(")

#don't read this, it's shit i've written :(
def matched(player, board):
    """
    Returns true if any player wins
    """
    to_find = "".join([player.mark]*3)

    #trying to find in rows
    for i in range(3):
        row = "".join(board[i])
        if row==to_find:
            print(f'matched in row {i}')
            return True
    #trying to find in cols
    dummy = board.transpose()
    for i in range(3):
        col = "".join(dummy[i])
        if col==to_find:
            print(f'matched in column {i}')
            return True
    #trying to find in main diagonal
    diag = "".join([board[i][i] for i in range(3)])
    if to_find==diag:
        print('found in diag')
        return True

    #trying to find in rev diagonal
    rdiag = "".join([board[i][2-i] for i in range(3)])
    if to_find==rdiag:
        print('found at revdiag')
        return True

def game_end():
    """
    This function will end the game or start a new game,
    depending on the user input.
    """
    rep= input('Game Ended!, want to play more? y/n: ')
    if rep=='y':
        play()
    else:
        return

def print_board(board):
    """
    This function will print the board after each turn
    """
    print("\n")
    print("\t     |     |")
    print(f"\t  {board[0][0]}  |  {board[0][1]}  |  {board[0][2]}")
    print('\t_____|_____|_____')
 
    print("\t     |     |")
    print(f"\t  {board[1][0]}  |  {board[1][1]}  |  {board[1][2]}")
    print('\t_____|_____|_____')
 
    print("\t     |     |")
 
    print(f"\t  {board[2][0]}  |  {board[2][1]}  |  {board[2][2]}")
    print("\t     |     |")
    print("\n")

if __name__ == '__main__':

    p1_name = input('Enter Player1 name: ')
    p2_name = input('Enter Player2 name: ')
    p1 = Player(p1_name, 'X')
    p2 = Player(p2_name, 'O')

    play(p1, p2)