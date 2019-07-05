#!/usr/bin/python3
# -*- coding: utf-8 -*-
import math

def premier(n):
    if n == 0: return(False)
    if n == 1: return(True)
    for i in range(2, n):
        if n % i == 0:
            return(False)
    return(True)
