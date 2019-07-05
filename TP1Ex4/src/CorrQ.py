#!/usr/bin/python3
# -*- coding: utf-8 -*-

#q1 - change 'r' to 'l'
def change(string):
    size = len(string)
    s = list(string)
    i = 0
    while i<size:
        if s[i]=='r':
            s[i]='l'
        i = i+1
    return "".join(s)

#q2 - supp
def changeSupp(string, x, y):
    size = len(string)
    s = list(string)
    i = 0
    while i<size:
        if s[i]==x:
            s[i]=y
        i = i+1
    return "".joint(s)
