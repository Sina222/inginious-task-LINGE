#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import CorrQ as corr
import q

INPUTS = [
    {
        "A": [[1, 0], [-1, 3]],
        "B": [[3], [1]]
    },
    {
        "A": [[1, 0], [-1, 3]],
        "B": [[3, 1], [2, 1]]
    },
    {
        "A": [[3]],
        "B": [[2]]
    },
    {
        "A": [[3]],
        "B": [[2, 3, 5]]
    },
    {
        "A": [[3, 1, 3, 5]],
        "B": [[2, 6, 5, 8], [42, 1, 6, 9], [5, 8, 4, 1], [3, 5, 6, 8]]
    }
]


class TestProduct(unittest.TestCase):
    def test_specs(self):
        self.assertTrue(hasattr(q, "produitMatrice") and callable(
            q.produitMatrice), _("Vous n'avez pas bien spécifié votre fonction"))

    def test_q1(self):
        for i in INPUTS:
            student = q.produitMatrice(i["A"], i["B"])
            sol = corr.produitMatrice(i["A"], i["B"])
            self.assertEqual(student, sol, _(
                "Pour les matrices A = {}, B = {}\nvotre code a produit : {}\nmais le résultat attendu est : {}".format(i["A"], i["B"], student, sol)))


if __name__ == '__main__':
    unittest.main()
