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

board = Plateau(8)
board.affichage()


saisieCoordonees = input(
    'rentrez les coordonnes du pion au format x y: ').split()

listresult = [int(i) for i in saisieCoordonees]
print(listresult)

pion1 = Pion(listresult[0], listresult[1], 'x')
pion2 = Pion(listresult[0], listresult[1], 'o')

# if a[listresult[0]][listresult[1]] == '.':
#     board.placerPion(pion2)
# else:
#     print('cette case est deja prise')

board.placerPion(pion1)

board.affichage()
