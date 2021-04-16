import random

movies = ['java','python','c++']

class Player:
    pts = 0
    def __init__(self, name):
        self.name = name
    def upPts(self):
        self.pts+=1

def play():
    p1Name = input('p1 name: ')
    p2Name = input('p2 name: ')

    p1 = Player(p1Name)
    p2 = Player(p2Name)

    turn = 0
    nextTurn = True

    while nextTurn:
        player_plays(p1)
        player_plays(p2)
        toPlay = input('want to play more? y/n: ')
        if toPlay=='n':
            nextTurn = False
        elif toPlay!='y':
            print('Noob, enter valid input')
        printScores(p1, p2)

def printScores(p1, p2):
    print(p1.name,":", p1.pts )
    print(p2.name,":", p2.pts )

def guess_check(player, pick_mov):
    guess = input('Whats it: ')
    if guess==pick_mov:
        print('correct guess')
        player.upPts()
    else:
        print('wrong guess!')

def player_plays(player):
    print(player.name, 'turn')
    pick_mov =  random.choice(movies)
    hint = "*"*len(pick_mov)
    print(hint)
    chosen = int(input('1 for guess, 2 for unmask: '))
    if chosen==1:
        guess_check(player, pick_mov)
    elif chosen==2:
        ch = input('check for letter: ')
        hint = Masked(hint, pick_mov, ch)
        print(hint)
        guess_check(player, pick_mov)
    else:
        print('Noob, enter valid input')

def Masked(hint, picked_mov, ch):
    temp= list(hint)
    for i in range(len(hint)):
        if(picked_mov[i]==ch):
            temp[i]=ch
    return "".join(temp)

play()