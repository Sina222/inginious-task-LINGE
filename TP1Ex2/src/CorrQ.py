#!/usr/bin/python3
# -*- coding: utf-8 -*-

def moyenne(a,b):
    return (a+b)/2

def main():
    a = int(input("Entrez le premier nombre :"))
    b = int(input("Entrez le deuxième nombre :"))
    print("La moyenne est :" + str(moyenne(a,b)))
