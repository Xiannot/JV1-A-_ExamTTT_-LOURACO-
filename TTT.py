
"""

def grille(tableau):
    tableau=[0,1,2,3,4,5,6,7,8]
    print(tableau)


grille()

"""

"""
def jeux():
    print("Le X commence")
    print("Dans quelle case souhaiter vous le poser?")
    print(tableau)
    choixcase1=int(input("A la case"))
    tableau.pop(choixcase1)     
    tableau.insert(choixcase1,"X")
    print(tableau)
    print("Autour du deuxième joueur")
    print("Dans quelle case souhaiter vous le poser?")
    print(tableau)
    choixcase2=int(input("A la case"))
    tableau.pop(choixcase2)
    tableau.insert(choixcase2,"0")
    print(tableau)

tableau=[0,1,2,3,4,5,6,7,8]

for i in range(len(tableau)):
    print("Pour plus de confort de jeux il est préférable de créer un tableau sur papier allant de gauche vers la droite en les nomants de 0 a 8")
    jeux()
"""

"""
def jeux():
    print("Le X commence")
    print("Dans quelle case souhaiter vous le poser?")
    print(tableau)
    choixcase1=int(input("A la case"))
    tableau.pop(choixcase1)     
    tableau.insert(choixcase1,"X")
    print(tableau)
    print("Autour du deuxième joueur")
    print("Dans quelle case souhaiter vous le poser?")
    print(tableau)
    choixcase2=int(input("A la case"))
    tableau.pop(choixcase2)
    tableau.insert(choixcase2,"0")
    print(tableau)
    return tableau

def win_verticale():
    if tableau[0] == "X":
        if tableau[1] == "X":
            if tableau[2] == "X":
                print("win de X")
    if tableau[3] == "X":
        if tableau[4] == "X":
            if tableau[5] == "X":
                print("win de X")
    if tableau[6] == "X":
        if tableau[7] == "X":
            if tableau[8] == "X":
                print("win de X")


    if tableau[0] == "0":
        if tableau[1] == "0":
            if tableau[2] == "0":
                print("win de 0")
    if tableau[3] == "0":
        if tableau[4] == "0":
            if tableau[5] == "0":
                print("win de 0")
    if tableau[6] == "0":
        if tableau[7] == "0":
            if tableau[8] == "0":
                print("win de 0")

def win_horizontale():
    if tableau[0] == "X":
        if tableau[3] == "X":
            if tableau[6] == "X":
                print("win de X")
    if tableau[1] == "X":
        if tableau[4] == "X":
            if tableau[7] == "X":
                print("win de X")
    if tableau[2] == "X":
        if tableau[5] == "X":
            if tableau[8] == "X":
                print("win de X")
                

    if tableau[0] == "0":
        if tableau[3] == "0":
            if tableau[6] == "0":
                print("win de 0")
    if tableau[1] == "0":
        if tableau[4] == "0":
            if tableau[7] == "0":
                print("win de 0")
    if tableau[2] == "0":
        if tableau[5] == "0":
            if tableau[8] == "0":
                print("win de 0")

def win_diagonale():
    if tableau[0] == "X":
        if tableau[4] == "X":
            if tableau[8] == "X":
                print("win de X")
    if tableau[6] == "X":
        if tableau[4] == "X":
            if tableau[2] == "X":
                print("win de X")
                

    if tableau[0] == "0":
        if tableau[4] == "0":
            if tableau[8] == "0":
                print("win de 0")
    if tableau[6] == "0":
        if tableau[4] == "0":
            if tableau[2] == "0":
                print("win de 0")

                
#--------------------------------------------------------------------------------


tableau=[0,1,2,3,4,5,6,7,8]
for i in range(10000):
    print("Pour plus de confort de jeux il est préférable de créer un tableau sur papier allant de gauche vers la droite en les nomants de 0 a 8")
    jeux()
    win_verticale()
    win_horizontale()
    win_diagonale()
"""

#---------------------------------------------------------------------------------

def jeux():
    print("Le X commence")
    print("Dans quelle case souhaiter vous le poser?")
    print(tableau)
    choixcase1=int(input("A la case"))
    tableau.pop(choixcase1)     
    tableau.insert(choixcase1,"X")
    print(tableau)
    print("Autour du deuxième joueur")
    print("Dans quelle case souhaiter vous le poser?")
    print(tableau)
    choixcase2=int(input("A la case"))
    tableau.pop(choixcase2)
    tableau.insert(choixcase2,"0")
    print(tableau)
    return tableau

def win_verticale():
    if tableau[0] == "X":
        if tableau[1] == "X":
            if tableau[2] == "X":
                print("win de X")
    if tableau[3] == "X":
        if tableau[4] == "X":
            if tableau[5] == "X":
                print("win de X")
    if tableau[6] == "X":
        if tableau[7] == "X":
            if tableau[8] == "X":
                print("win de X")


    if tableau[0] == "0":
        if tableau[1] == "0":
            if tableau[2] == "0":
                print("win de 0")
    if tableau[3] == "0":
        if tableau[4] == "0":
            if tableau[5] == "0":
                print("win de 0")
    if tableau[6] == "0":
        if tableau[7] == "0":
            if tableau[8] == "0":
                print("win de 0")

def win_horizontale():
    if tableau[0] == "X":
        if tableau[3] == "X":
            if tableau[6] == "X":
                print("win de X")
    if tableau[1] == "X":
        if tableau[4] == "X":
            if tableau[7] == "X":
                print("win de X")
    if tableau[2] == "X":
        if tableau[5] == "X":
            if tableau[8] == "X":
                print("win de X")
                

    if tableau[0] == "0":
        if tableau[3] == "0":
            if tableau[6] == "0":
                print("win de 0")
    if tableau[1] == "0":
        if tableau[4] == "0":
            if tableau[7] == "0":
                print("win de 0")
    if tableau[2] == "0":
        if tableau[5] == "0":
            if tableau[8] == "0":
                print("win de 0")

def win_diagonale():
    if tableau[0] == "X":
        if tableau[4] == "X":
            if tableau[8] == "X":
                print("win de X")
    if tableau[6] == "X":
        if tableau[4] == "X":
            if tableau[2] == "X":
                print("win de X")
                

    if tableau[0] == "0":
        if tableau[4] == "0":
            if tableau[8] == "0":
                print("win de 0")
    if tableau[6] == "0":
        if tableau[4] == "0":
            if tableau[2] == "0":
                print("win de 0")


tableau=[0,1,2,3,4,5,6,7,8]
for i in range(9): #Pour le nombre de case avant que le jeux soit complets
    print("Pour plus de confort de jeux il est préférable de créer un tableau sur papier allant de gauche vers la droite en les nomants de 0 a 8")
    jeux()
    win_verticale()
    win_horizontale()
    win_diagonale()


#Pour réaliser un puissance 4 se qui nous reste a faire c'est de agrandir la longueur de la case a 8 max et 8 de hauteur et de changer le nombre d'alignement de 3 a 4