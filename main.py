"""def affichage_d_une_grille_de_merde_avec_des_petits_points(i, j):
    cases = []
    n = 0
    for a in range(i):
        if a == 0:
            print(n)
            for b in range(j):
                if b == 0:
                    print (n)
                n += 1
                if b > 0:
                    print('.')
affichage_d_une_grille_de_merde_avec_des_petits_points(8,8)"""

def test():
    i = 0
    j = 0
    n = 0
    while i != 8:
        while j != 8:
            print ('.', end=" ")
            j += 1
        print('\n', end="")
        j = 0
        i += 1
test()