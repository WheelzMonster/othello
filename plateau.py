from pion import Pion


class Plateau:
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

    def affichage(self):
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

    def placerPion(self, Pion):
        self.cases[Pion.axex][Pion.axey] = Pion.equipe
    
#haut    = [0, -1]
#bas     = [0, 1]
#gauche  = [-1, 0]
#droite  = [1, 0]
#diag hg = [-1, -1]
#diag hd = [1, -1]
#diag bg = [-1, 1]
#diag bd = [1, 1]

    def case_voisine(self, direction, pion):
        posx = pion[0] + direction[0]
        posy = pion[1] + direction[1]
        #equipe = self.cases[posx][posy]
        pos_case_voisine = [posx, posy, self.cases[posx][posy]]
        return pos_case_voisine

    def pionRetourne(self, pion):
        case = []
        case.append(pion.axex)
        case.append(pion.axey)
        equipe = pion.equipe
        direction = []
        liste_a_retourner = []
        for xdirection, ydirection in [[0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1]]:
            direction.append(xdirection)
            direction.append(ydirection)
            last_pos = self.case_voisine(direction, case)
            liste_temporaire = []
            while last_pos[2] != equipe and last_pos[2] != ' .' and not last_pos[2].strip().isnumeric() and last_pos[2] != "  ":
                liste_temporaire.append(last_pos)
                last_pos = self.case_voisine(direction, last_pos)
            direction.clear()
            if last_pos[2] == equipe:
                for p in liste_temporaire:
                    liste_a_retourner.append(p)
        return liste_a_retourner

    def retourne(self, liste, turn):
        if turn % 2 == 0:
            for x in liste:
                self.cases[x[0]][x[1]] = ' X'
        elif turn % 2 != 0:
            for x in liste:
                self.cases[x[0]][x[1]] = ' O'

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