def maxmatrice(mat):
    """
    cette fonction recoit une matrice d'entiers en entree 
    et qui renvoie en sortie un entier qui est la valeur 
    du plus grand element de la matrice.
    """    
    
    #initialiser le maximum comme etant la valeur du premier element
    valmax = mat[0][0]
    for i in range(len(mat)): 
        for j in range(len(mat[0])): 
            if (mat[i][j] > valmax):
                valmax = mat[i][j]
    return valmax     

