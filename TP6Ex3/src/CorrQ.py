def examen(notes):
    maxi = notes[0]
    mini = notes[0]
    moy = 0
    nombre = [0 for i in range(10)]
    for i in range(len(notes)):
        moy+=notes[i]
        nombre[notes[i]//10]+=1
        if notes[i]>maxi:
            maxi=notes[i]
        if notes[i]<mini:
            mini=notes[i]
    print("La note maximale est " + str(maxi))
    print("La note minimale est " + str(mini))
    print("La moyenne des notes est " + str(moy/len(notes)))
    return nombre

def launch(notes):
    tab = examen(notes)
    for i in range(len(tab)):
        print("il y a " + str(tab[i]) + " notes entre " + str(i*10) + " et " + str(i*10+9))