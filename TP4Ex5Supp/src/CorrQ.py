def ligsomme(mat):
    """
    cette fonction recoit une matrice d'entiers en entree  et qui renvoie en sortie la somme de chaque ligne de
    la matrice
    """   
    s =[0 for i in range(len(mat))]
        
    if len(mat) != len(mat[0]):
        print("la matrice n'est pas carree, 0 est renvoye")
    else:
        for i in range(len(mat)): 
            for j in range(len(mat[0])):    
                s[i]+=mat[i][j]   
        return s
