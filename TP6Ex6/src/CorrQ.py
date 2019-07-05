#!/usr/bin/python3
# -*- coding: utf-8 -*-


def produitMatrice(A, B):
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            product = 0
            for v in range(len(B)):
                product += A[i][v] * B[v][j]
            row.append(product)
        result.append(row)
    return result
