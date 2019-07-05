import math 

def trajectoire(mat):
    x=0 #Position de la ligne
    nbdiag=0 #Compteur du nombre de déplacements en diagonale
    #Recherche du point de départ
    while mat[x][0]!=1:
        x+=1
    #Boucle for sur la position y (colonne)
    for y in range(1,len(mat[0])):
        #Test des deux positions en diagonale, si l'une d'entre elles contient un 1, on met à jour la position en x et on incrémente le compteur de mouvements en diagonale.
        if (x>0 and mat[x-1][y]==1):
            x-=1
            nbdiag+=1

        if (x<len(mat)-1 and mat[x+1][y]==1):
            x+=1
            nbdiag+=1
    return math.sqrt(2)*nbdiag + len(mat[0])-1 - nbdiag

M=[
[0,0,0,0,0,1,0,0,0,0,1,0,0,1,0,0,1,0],
[0,0,1,1,0,0,0,0,0,1,0,1,0,0,0,0,1,0],
[0,0,1,1,1,0,0,1,1,0,0,0,1,1,1,0,0,0],
[0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,0,0],
[1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0],
[0,1,0,0,1,0,0,1,0,1,1,1,0,0,0,0,0,1],
[0,0,1,1,0,0,0,0,0,1,1,1,0,0,0,1,0,0]
]

print("La longueur totale du parcours dans le tableau est {}".format(trajectoire(M)))