from pion import Pion
from partie import Partie
from plateau import Plateau

def gameLoop():

    game = True
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