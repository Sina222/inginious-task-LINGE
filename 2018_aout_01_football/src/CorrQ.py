#!/usr/bin/python3
# -*- coding: utf-8 -*-
import math

def arret(but):
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

