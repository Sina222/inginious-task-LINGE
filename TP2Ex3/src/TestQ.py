#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import CorrQ as corr
import q

INPUTS = [
    { "v": 62, "vmax": 50 },
    { "v": 53, "vmax": 50 },
    { "v": 0, "vmax": 50 },
    { "v": 51, "vmax": 50 },
    { "v": 1, "vmax": 1 },
    { "v": 2, "vmax": 1 },
]


class TestAmende(unittest.TestCase):
    def test_specs(self):
        self.assertTrue(hasattr(q, "amende") and callable(
            q.amende), _("Vous n'avez pas bien spécifié votre fonction"))

    def test_q1(self):
        for i in INPUTS:
            student = q.amende(i["vmax"], i["v"])
            sol = corr.amende(i["vmax"], i["v"])
            self.assertEqual(student, sol, _(
                "Pour vmax = {} et v = {}\nvotre code a produit : {}\nmais le résultat attendu est : {}".format(i["vmax"], i["v"], student, sol)))


if __name__ == '__main__':
    unittest.main()
