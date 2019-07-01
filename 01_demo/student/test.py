from student_code import arret
import math

def arret_good(but):
    hb,lb,lg=0,0,0
    output=[0,0,0]
    for h in range(len(but)): #until H
        for l in range(len(but[0])): #until L
            if but[h][l]=='B':
                hb,lb=h,l
            elif but[h][l]=='G':
                hg,lg=0,l
    # //Gestion de la direction
    if lb<lg:
        output[0]=-1.0
    else:
        if (lg!=lb):
            output[0]=1.0

    #Calcul de la distance
    output[2]=math.sqrt((hb**2)+(lg-lb)**2)

    #Calcul de l'angle

    if (lg==lb):
        output[1]=90
    else:
        output[1]=math.degrees(math.atan(hb/(abs(lg-lb))))
    return output


if __name__ == "__main__":
    H=10
    L=20
    BUT=[['X' for j in range(0,L)] for i in range(0,H)]
    BUT[6][5]='G'
    BUT[3][14]='B'
    res=arret(BUT)
    res_good = arret_good(BUT)
    if res == res_good:
        print("True")
    else:
        print("La bonne réponse B en [3][14] et G en [6][5] est la direction {} avec un angle de {} sur une distance de {}".format(res_good[0],res_good[1],res_good[2]))
