#!/usr/bin/python3
# -*- coding: utf-8 -*-


def amende(vmax, v):
    if v > vmax:
        result = (v - vmax) * 5
        if v - vmax > 10:
            result *= 2
        return max(12.5, result)
    return 0
