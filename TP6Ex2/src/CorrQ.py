#!/usr/bin/python3
# -*- coding: utf-8 -*-


def tempete(M):
    return [sum([1 if (M[i][0] > 90 and M[i][1] > 10 ) else  0 for i in range(24)])] + [round(sum([M[i][0]/24 for i in range(24)]),2)] + [round(sum([M[i][1]/24 for i in range(24)]),2)]
