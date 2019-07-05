def populationIterative(a,n):
    if n <= 0:
        return 0
    popu = a
    for i in range(1,n):
        popu = 2*popu
    return popu
def nombreAnnee():
    nbAnnee = 0
    while 20*populationIterative(3, nbAnnee) < 600000:
        nbAnnee += 1
    return nbAnnee

    

