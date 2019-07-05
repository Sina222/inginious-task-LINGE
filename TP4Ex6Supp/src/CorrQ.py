def colsomme(mat):
    """
    cette fonction recoit une matrice d'entiers en entree et qui renvoie en sortie la somme de chaque colonne de
    la matrice
    """    
    s =[0 for i in range(len(mat[0]))]
        
    if len(mat) != len(mat[0]):
        return None
    else:
        for i in range(len(mat)): 
            for j in range(len(mat[0])): 
                s[j]+=mat[i][j]
    return s