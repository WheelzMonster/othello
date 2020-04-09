from pion import Pion
from plateau import Plateau


class Partie:
    def __init__(self, dimension):
        self.plateau = Plateau(dimension)

    def coupJoue(self, turn):
        saisieCoordonees = input(
            'rentrez les coordonnes du pion au format x y: ').split()

        listresult = [int(i) for i in saisieCoordonees]

        if turn % 2 == 0:
            pion = Pion(listresult[0], listresult[1], ' O')
        elif turn % 2 != 0:
            pion = Pion(listresult[0], listresult[1], ' X')

        listresult.clear()
        return pion
