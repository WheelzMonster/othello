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
a = [[" ", "1", "2", "3", "4", "5", "6", "7", "8"], ["1", ".", ".", ".", ".", ".", ".", ".", "."], ["2", ".", ".", ".", ".", ".", ".", ".", "."], ["3", ".", ".", ".", ".", ".", ".", ".", "."], ["4", ".", ".", ".", "x", "o", ".", ".", "."], ["5", ".", ".", ".", "o", "x", ".", ".", "."], ["6", ".", ".", ".", ".", ".", ".", ".", "."], ["7", ".", ".", ".", ".", ".", ".", ".", "."], ["8", ".", ".", ".", ".", ".", ".", ".", "."]]
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()
x, y = int(input('veuillez mettre les coordonnées a laquelle vous souhaitez mettre votre pion au format "x,y"\n'))