#!/usr/bin/python3
# -*- coding: utf-8 -*-


def triangle3(n):
    for i in range(n+1):
        for j in range(1,n-i+1):
            print(" ",end=" ")
        for j in range(1,2*i):
            print("*", end=" ")
        print()

triangle3(0)
