from pion import Pion


class Plateau:
    def __init__(self, dimensions):
        self.dimensions = dimensions
        self.n = dimensions
        self.m = dimensions
        self.cases = [[' .'] * self.m for i in range(self.n)]

    def affichage(self):

        self.cases[0][0] = '  '
        self.cases[self.dimensions // 2][self.dimensions // 2] = ' O'
        self.cases[self.dimensions // 2][self.dimensions // 2 + 1] = ' X'
        self.cases[self.dimensions // 2 + 1][self.dimensions // 2] = ' X'
        self.cases[self.dimensions // 2 + 1][self.dimensions // 2 + 1] = ' O'

        p = 1
        for i in range(1, self.dimensions):
            if i <= 9:
                self.cases[p][0] = " " + str(i)
            else:
                self.cases[p][0] = "" + str(i)  # vertical
            self.cases[0][p] = " " + str(i)  # horizontal
            p += 1

        for x in self.cases:
            print(' '.join(x))

    def isGameDone(self):
        print('le jeu est finis')

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
        posx = pion.axex + direction[0]
        posy = pion.axey + direction[1]
        print (posx, posy)
        equipe = self.cases[posx][posy]
        pos_case_voisine = [posx, posy, equipe]
        print(pos_case_voisine)
        return pos_case_voisine

    def pionRetourne(self, pion):
        case = pion[pion.axex][pion.axey]
        equipe = pion.equipe
        direction = []
        for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
            last_pos = case_voisine(direction, pion)
            liste_a_retourner = []
            while last_pos[2] != equipe:
                liste_a_retourner.append(last_pos)
                last_pos = case_voisine(direction, last_pos)
            if last_pos[2] == equipe:
                return liste_a_retourner