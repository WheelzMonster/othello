from pion import Pion
from partie import Partie
from plateau import Plateau



def gameLoop():

    game = True
    userBoardChoice = int(input(
        "choisissez la longueur de votre tableau (4, 6, 8 ou 10): "))
    while userBoardChoice != 4 and userBoardChoice != 6 and userBoardChoice != 8 and userBoardChoice != 10:
        userBoardChoice = int(input(
        "choisissez la longueur de votre tableau (4, 6, 8 ou 10): "))

    partie = Partie(userBoardChoice+1)
    partie.plateau.affichage()
    turn = 0
    Pion.equipe = " X"
    while game:
        pion = partie.coupJoue(turn)
        # if a[listresult[0]][listresult[1]] == '.':
        #     board.placerPion(pion2)
        # else:
        #     print('cette case est deja prise')


        while partie.plateau.cases[pion.axex][pion.axey] != " .":
            print("vous ne pouvez pas jouer ici, cette case est deja jouee")
            pion = partie.coupJoue(turn)
        partie.plateau.placerPion(pion)

        partie.plateau.affichage()
        
        turn += 1


gameLoop()
#partie = Partie(6)
#partie.plateau.affichage()
#MonPion = Pion(4, 4, ' X')

#partie.plateau.case_voisine([1, -1], MonPion)