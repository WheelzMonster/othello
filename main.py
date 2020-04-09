from plateau import Plateau
from pion import Pion
from partie import Partie

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


def gameLoop():

    game = True
    userBoardChoice = int(input(
        "choisissez la longueur l de votre tableau (si vous choisissez 8, vous aurez une grille de 8 x 8): "))

    partie = Partie(userBoardChoice+1)
    partie.plateau.affichage()
    while game:
        pion = partie.coupJoue()
        # if a[listresult[0]][listresult[1]] == '.':
        #     board.placerPion(pion2)
        # else:
        #     print('cette case est deja prise')

        partie.plateau.placerPion(pion)
        partie.plateau.affichage()


gameLoop()

# testing ssh key again again
