#!/usr/bin/python3
# -*- coding: utf-8 -*-


def main():

    #variables initialisation
    names = [] #list for the name
    first_boucle = True #bool variable for the first loop
    second_boucle = True #bool variable for the second loop

    #first loop
    while first_boucle :
        # read the input
        print_names(names)
        name = input("Enter the name :")
        # sort the list
        if(name != ""):
            sort(names,name)
        else:
            first_boucle = False

    #second boucle
    while second_boucle :
        # read the input
        print_names(names)
        n = int(input("Enter the id of the name to remove :"))
        #remove the name
        if(n>0 and n<len(names)):
            names = names[:n] + names[n+1:]
        elif(n>=len(names)):
            print("You are out of the list !")
        elif(n == 0):
            names = names[1:]
        else:
            second_boucle = False
            print("Goodbye !")

def sort(names, name):
    """
        Insertion sort
        name : is a list empty or not of string
        in : is the name to insert in the list
    """
    if(names == []) :
        names.append(name)
    else:
        i = 0
        not_insert = True
        while not_insert :
            if(i == len(names)):
                names.append(name)
                not_insert = False
            elif(name <= names[i]):
                names.insert(i,name)
                not_insert = False
            i += 1


def print_names(names):
    """
        print the names in a elegant way
        names : list of string to print
    """
    if( names != []):
        for i in range(len(names)):
            print(str(i) + " : " + names[i])
