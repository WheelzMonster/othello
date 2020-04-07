"""
def test(ln):
    i = 0
    j = 0
    a = [[]]
    while i != ln:
        while j != ln:
            print ('.', end=" ")
            j += 1
        print('\n', end="")
        j = 0
        i += 1
test(8)
"""
a = [[" ", "1", "2", "3", "4", "5", "6", "7", "8"], ["1", ".", ".", ".", ".", ".", ".", ".", "."], ["2", ".", ".", ".", ".", ".", ".", ".", "."], ["3", ".", ".", ".", ".", ".", ".", ".", "."], ["4", ".", ".", ".",
                                                                                                                                                                                                  "x", "o", ".", ".", "."], ["5", ".", ".", ".", "o", "x", ".", ".", "."], ["6", ".", ".", ".", ".", ".", ".", ".", "."], ["7", ".", ".", ".", ".", ".", ".", ".", "."], ["8", ".", ".", ".", ".", ".", ".", ".", "."]]
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()

saisieCoordonees = input(
    'rentrez les coordonnes du pion au format x y: ').split()

listresult = [int(i) for i in saisieCoordonees]
print(listresult)
