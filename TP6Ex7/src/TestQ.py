#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import CorrQ as corr
import q


class TestNenuphare(unittest.TestCase):
    
    def test_specs_q1(self):
        self.assertTrue(hasattr(q, 'populationIterative') and callable(
            q.populationIterative), "@1@: " + _("Vous n'avez pas bien spécifié votre fonction."))

    def test_specs_q2(self):
        self.assertTrue(hasattr(q, 'nombreAnnee') and callable(
            q.nombreAnnee), "@2@: " + _("Vous n'avez pas bien spécifié votre fonction."))

    def test_q1(self):
        try:
            sol = corr.populationIterative(3, 6)
            sol2 = corr.populationIterative(0, 5)
            sol3 = corr.populationIterative(-4, 4)
            sol4 = corr.populationIterative(5, 7)
        except Exception as e:
            self.fail("@1@: " + str(e))
        try:
            stu = q.populationIterative(3, 6)
            stu2 = q.populationIterative(0, 5)
            stu3 = q.populationIterative(-4, 4)
            stu4 = q.populationIterative(5, 7)
        except Exception as e:
            self.fail("@1@: " + str(e))
        self.assertEqual(sol, stu, "@1@: Votre fonction ne calcule pas la bonne valeur")
        self.assertEqual(sol2, stu2, "@1@: Votre fonction ne gère pas correctement le cas n=0")
        self.assertEqual(sol3, stu3, "@1@: Votre fonction ne calcule pas la bonne valeur si n est négatif")
        self.assertEqual(sol4, stu4, "@1@: Votre fonction ne calcule pas la bonne valeur")

    def test_q2(self):
        try:
            sol = corr.nombreAnnee()
        except Exception as e:
            self.fail("@2@: " + str(e))
        try:
            stu = q.nombreAnnee()
        except Exception as e:
            self.fail("@2@: " + str(e))
        self.assertEqual(sol, stu, "@1@: Votre fonction ne calcule pas la bonne valeur")

if __name__ == '__main__':
	unittest.main()
