#!/usr/bin/python3
# -*- coding: utf-8 -*-

def main():
    eq = False
    for i in range(3):
        n = int(input("Entrez le numero " + str(i+1) + " :"))
        if i == 0 :
            max = n
        else:
            if n > max :
                max = n
            elif n == max :
                eq = True
    print("Le nombre le plus grand est " + str(max))
    if eq :
        print("Mais vous avez introduit des valeurs identiques !")
