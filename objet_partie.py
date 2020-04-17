from objet_pion import Pion
from objet_plateau import Plateau


class Partie:
    def __init__(self, dimension):
        # créer une partie avec un objet plateau en attribut
        self.plateau = Plateau(dimension)

    def coupJoue(self, turn):  # permet a l'utilisateur de rentrer les coordonnées de son pion et ça créer un pion x ou o en fonction du tours
        if turn % 2 == 0:
            saisieCoordonees = input(
                "c'est au tour des X de jouer \nrentrez les coordonnes du pion au format x y: ").split()
            while int(saisieCoordonees[0]) >= (self.plateau.dimensions) or int(saisieCoordonees[1]) >= (self.plateau.dimensions):
                saisieCoordonees = input(
                    "coordonnées invalides, vous êtes en dehors de la grille, c'est toujours au tour des X de jouer \nrentrez les coordonnes du pion au format x y: ").split()
        elif turn % 2 != 0:
            saisieCoordonees = input(
                "c'est au tour des O de jouer \nrentrez les coordonnes du pion au format x y: ").split()
            while int(saisieCoordonees[0]) >= (self.plateau.dimensions) or int(saisieCoordonees[1]) >= (self.plateau.dimensions):
                saisieCoordonees = input(
                    "coordonnées invalides, vous êtes en dehors de la grille, c'est toujours au tour des O de jouer \nrentrez les coordonnes du pion au format x y: ").split()

        listresult = [int(i) for i in saisieCoordonees]

        if turn % 2 == 0:
            pion = Pion(listresult[0], listresult[1], ' X')
        elif turn % 2 != 0:
            pion = Pion(listresult[0], listresult[1], ' O')

        listresult.clear()
        return pion
