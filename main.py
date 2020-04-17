from objet_pion import Pion
from objet_partie import Partie
from objet_plateau import Plateau


def gameLoop():

    game = True
    userBoardChoice = int(input(
        "choisissez la longueur de votre tableau (4, 6, 8 ou 10): "))
    while userBoardChoice != 4 and userBoardChoice != 6 and userBoardChoice != 8 and userBoardChoice != 10:
        userBoardChoice = int(input(
            "Saisie incorrecte, veuillez choisir la longueur de votre tableau dans les options suivantes (4, 6, 8 ou 10): "))

    partie = Partie(userBoardChoice+1)
    partie.plateau.affichage()
    turn = 0
    while game:
        pion = partie.coupJoue(turn)
        while partie.plateau.cases[pion.axex][pion.axey] != " .":
            print("vous ne pouvez pas jouer ici, cette case est deja jouee")
            pion = partie.coupJoue(turn)

        liste = partie.plateau.pionRetourne(pion)
        while not liste:
            print("vous ne pouvez pas jouer ici car vous ne retournez aucun pion adverse")
            pion = partie.coupJoue(turn)
            liste = partie.plateau.pionRetourne(pion)

        partie.plateau.placerPion(pion)
        partie.plateau.retourne(liste, turn)

        partie.plateau.affichage()
        gagnant = partie.plateau.finDePartie()

        total = (userBoardChoice) * (userBoardChoice)
        if gagnant[0] == 0:
            print("Bravo ! les O ont gagnés !")
            game = False
        elif gagnant[1] == 0:
            print("Bravo ! Les X ont gagnés !")
            game = False
        elif gagnant[0] < gagnant[1] and gagnant[0] + gagnant[1] == total:
            print("Bravo ! Les O ont gagnés !")
            game = False
        elif gagnant[0] > gagnant[1] and gagnant[0] + gagnant[1] == total:
            print("Bravo ! Les X ont gagnés !")
            game = False
        turn += 1


gameLoop()
