#!/usr/bin/python3
# -*- coding: utf-8 -*-

def compte():
    liste = [0 for i in range(10)]
    n=int(input("Entrer les nombres (compris entre 0 et 9, -1 pour quitter) :"))
    while n != -1:
        liste[n]+=1
        n = int(input()) 
    for i in range(len(liste)):   
        if liste[i] != 0:
            print("le nombre {} est introduit {} fois".format(i,liste[i]))

