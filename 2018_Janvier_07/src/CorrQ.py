#!/usr/bin/python3
# -*- coding: utf-8 -*-

def PayeTaxi(mat,prix):
    best=0
    result=[0,0]
    Manhattan=[0 for i in range(len(mat))]
    for i in range(len(mat)):
        Manhattan[i]=abs(mat[i][1]-mat[i][3])+abs(mat[i][2]-mat[i][4])
        result[0] +=Manhattan[i]*prix
        if best<Manhattan[i]:
            best=Manhattan[i]
            result[1]=i+1;
    return result
