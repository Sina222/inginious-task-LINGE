#!/usr/bin/python3
# -*- coding: utf-8 -*-


def ajoutPrenom(liste, prenom):
    if not prenom in liste:
        poss = 0
        while (poss < len(liste)) and (prenom > liste[poss]):
            poss += 1
        liste.insert(poss,prenom)
    
    print(liste)
