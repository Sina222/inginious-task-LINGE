#!/usr/bin/python3
# -*- coding: utf-8 -*-

import df

def integrale(a,b,nbPoints):
    dx = (b-a) / float(nbPoints-1)
    approx = (df.f(float(a)) + df.f(float(b))) *dx/2.0
    for i in range(1, nbPoints-2):
        approx = approx + dx*df.f(a+i*dx)

    return approx
