from plateau import Plateau
from pion import Pion

"""
def test(ln):
    i = 0
    j = 0
    a = [[]]
    while i != ln:
        while j != ln:
            print ('.', end=" ")
            j += 1
        print('\n', end="")
        j = 0
        i += 1
test(8)
"""

userBoardChoice = int(input(
    "choisissez la longueur l de votre tableau (si vous choisissez 8, vous aurez une grille de 8 x 8): "))

board = Plateau(userBoardChoice)
board.affichage()


def gameLoop():

    game = True
    turn = 0

    while game:
        saisieCoordonees = input(
            'rentrez les coordonnes du pion au format x y: ').split()

        listresult = [int(i) for i in saisieCoordonees]

        if turn % 2 == 0:
            pion = Pion(listresult[0], listresult[1], 'x')
        else:
            pion = Pion(listresult[0], listresult[1], 'o')

        # if a[listresult[0]][listresult[1]] == '.':
        #     board.placerPion(pion2)
        # else:
        #     print('cette case est deja prise')

        board.placerPion(pion)
        board.affichage()
        turn += 1
        listresult.clear()


gameLoop()

# testing ssh key again
