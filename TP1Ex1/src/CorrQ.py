#!/usr/bin/python3
# -*- coding: utf-8 -*-

def heure(nbseconde):
    #Transforme les secondes en heure, minute et seconde
    heure, minute, seconde,reste=0,0,0,0
    heure = nbseconde // 3600
    reste = nbseconde % 3600
    minute = reste // 60
    seconde = reste % 60
    #Print resultat
    print("{} heures, {} minutes et {} secondes".format(heure, minute, seconde))
    