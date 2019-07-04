#!/usr/bin/python3
# -*- coding: utf-8 -*-


def piloteLePlusRapide(x, n):
    victoires =[0 for i in range(len(x))]
    for k in range(n):
        for j in range(len(x[0])):
            victoires[vainqueur(x, j, len(x[0][0])-1-k)]+=1
    max = victoires[0]
    champion = 0
    for i in range(len(victoires)):
        if victoires[i] > max:
            max = victoires[i]
            champion = i
        elif victoires[i] == max:
            champion = -1
    return champion


def vainqueur(x, j, k):
    temps = [0 for i in range(len(x))]
    for i in range(len(x)):
        temps[i] = x[i][j][k]
    min = temps[0]
    vainqueur = 0

    for i in range(len(x)):
        if temps[i] < min:
            min = temps[0]
            vainqueur = i
    return vainqueur
