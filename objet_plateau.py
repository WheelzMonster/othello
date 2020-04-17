from objet_pion import Pion


class Plateau:
    # créer un plateau avec les dimensions choisies par le joueur et place les 4 pions de départ
    def __init__(self, dimensions):
        self.dimensions = dimensions
        self.n = dimensions + 1
        self.m = dimensions + 1
        self.cases = [[' .'] * self.m for i in range(self.n)]
        self.cases[self.n - 1][0] = '  '
        self.cases[0][self.n - 1] = '  '
        self.cases[self.n - 1][self.n - 1] = '  '
        self.cases[0][0] = '  '
        self.cases[self.dimensions // 2][self.dimensions // 2] = ' O'
        self.cases[self.dimensions // 2][self.dimensions // 2 + 1] = ' X'
        self.cases[self.dimensions // 2 + 1][self.dimensions // 2] = ' X'
        self.cases[self.dimensions // 2 + 1][self.dimensions // 2 + 1] = ' O'

    def affichage(self):  # permet d'afficher la grille apres sa création
        p = 1
        for i in range(1, self.dimensions):
            if i <= 9:
                self.cases[p][0] = " " + str(i)
                self.cases[self.n - 1][p] = " " + str(i)
                self.cases[p][self.n - 1] = " " + str(i)
            else:
                self.cases[p][0] = "" + str(i)  # vertical

                self.cases[self.n - 1][p] = " " + str(i)
                self.cases[p][self.n - 1] = " " + str(i)
            self.cases[0][p] = " " + str(i)  # horizontal
            p += 1

        for x in self.cases:
            print(' '.join(x))

    def placerPion(self, Pion):  # prend un objet pon en paramètre et le place sur la grille
        self.cases[Pion.axex][Pion.axey] = Pion.equipe

# haut    = [0, -1]
# bas     = [0, 1]
# gauche  = [-1, 0]
# droite  = [1, 0]
# diag hg = [-1, -1]
# diag hd = [1, -1]
# diag bg = [-1, 1]
# diag bd = [1, 1]

    # permet d'obtenir les coordonnées de la case voisine du pion rentré en paramètre qui se trouve à la direction rentrée en paramètre
    def case_voisine(self, direction, pion):
        posx = pion[0] + direction[0]
        posy = pion[1] + direction[1]
        pos_case_voisine = [posx, posy, self.cases[posx][posy]]
        return pos_case_voisine

    # permet d'obtenir une liste contenant les coordonnées des pions à retourner lors du placement d'un pion
    def pionRetourne(self, pion):
        case = []
        case.append(pion.axex)
        case.append(pion.axey)
        equipe = pion.equipe
        direction = []
        liste_a_retourner = []
        # une boucle qui regarde dans toutes les directions possibles
        for xdirection, ydirection in [[0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1]]:
            direction.append(xdirection)
            direction.append(ydirection)
            last_pos = self.case_voisine(direction, case)
            liste_temporaire = []
            # continue tant qu'il y a des pions inintérompue à retourner dans une même direction
            while last_pos[2] != equipe and last_pos[2] != ' .' and not last_pos[2].strip().isnumeric() and last_pos[2] != "  ":
                liste_temporaire.append(last_pos)
                last_pos = self.case_voisine(direction, last_pos)
            direction.clear()
            if last_pos[2] == equipe:
                for p in liste_temporaire:
                    liste_a_retourner.append(p)
        return liste_a_retourner

    def retourne(self, liste, turn):  # prend en paramètre une liste qui contient les coordonnées de pion à retourner, et en fonction du tour actuel (x ou o) change les pions aux coordonnées de cette liste en pion de l'équipe dont c'est le tour
        if turn % 2 == 0:
            for x in liste:
                self.cases[x[0]][x[1]] = ' X'
        elif turn % 2 != 0:
            for x in liste:
                self.cases[x[0]][x[1]] = ' O'

    # compte le nombre de x et de o sur le plateau et retourne ces 2 nombres dans une liste
    def finDePartie(self):
        nbX = 0
        nbO = 0
        gagnant = []
        for i in self.cases:
            for j in i:
                if j == " X":
                    nbX += 1
                if j == " O":
                    nbO += 1
        gagnant.append(nbX)
        gagnant.append(nbO)
        return gagnant
