def prix (sectionEntree, sectionSortie):
    prix=0.0
    if sectionEntree == sectionSortie:
        prix = 0.0
    else:
        prix = 1 + 0.5*(sectionSortie-sectionEntree-1)
    return prix
"""
x=int(input("Entrez la section d'entrée : "))
y=int(input("Entrez la section de sortie : "))
print("Le prix est de " + str(prix(x,y))+ " €")
"""