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
