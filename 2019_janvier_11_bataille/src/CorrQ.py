#!/usr/bin/python3
# -*- coding: utf-8 -*-


def bataille(a,b):
    j1 = []
    j2 = []
    cj1 = []
    cj2 = []
    win=1
    
    # Copie la liste des cartes des deux joueurs
    for i in range(len(a[0])):
        # Change la valeur de l'as
        if a[0][i] == 1:
            a[0][i]=14
        
        if(b[0][i] == 1):
            b[0][i]=14
        
        j1.append(a[0][i])
        j2.append(b[0][i])
        cj1.append(a[1][i])
        cj2.append(b[1][i])

    while (not (((len(j1)==0)==True and  (len(j2)==0)==False) or ((len(j1)==0)==False and (len(j2)==0)==True))):      
        c1 = j1[0]
        c2 =j2[0]
        a1 = cj1[0]
        a2 =cj2[0]

        if ((c1 > c2) or ((c1 == c2) and (a1 < a2))):
            j1.append(c1)
            j1.append(c2)
            cj1.append(c1)
            cj1.append(c2)

        if ((c1 < c2) or ((c1 == c2) and (a1 > a2))):
            j2.append(c1)
            j2.append(c2)
            cj2.append(c1)
            cj2.append(c2)

        j1.pop(0)
        j2.pop(0)
        cj1.pop(0)
        cj2.pop(0)
    
    if len(j1)==0:
        win = 2
    return win
