#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random
import sys
import filecmp

import q
import CorrQ as corr

CORRECT = ([1], 1, "Votre programme ne retourne pas la bonne somme pour une liste de taille 1.")
CORRECT_SAME = ([2,2,2,2,2,2],12,"Votre programme ne retourne pas la bonne somme pour une liste avec les mêmes numéros")
CORRECT_NEG = ([1,-1], 0, "Votre programme ne retourne pas la bonne somme pour une liste avec des valeurs négatives")

TESTS = [CORRECT, CORRECT_SAME, CORRECT_NEG]


class TestExtractor(unittest.TestCase):
    def test_exist(self):
        self.assertTrue(hasattr(q, 'sumArray'), ("You did not name the method as expected."))

    def test_cases(self):
        for t in TESTS:
            ans = t[2]
            corr_ans = t[1]
            stu_ans = q.sumArray(t[0])
            self.assertEqual(corr_ans, stu_ans, ans)
    
    def test_random(self):
        for i in range(5): #5 random list
            array = []
            for i in range(10): #list of size 10
                array.append(random.randint(0,100))
            self.assertEqual(q.sumArray(array), sum(array), "La somme de {} est {}".format(array,sum(array)))

    def test_print(self):
        original = sys.stdout
        array = []
        for i in range(100): #list of size 100
                array.append(random.randint(0,100))
        with open('redirect_corr.txt', 'w') as f:
            sys.stdout = f
            corr.sumArray(array)
        with open('redirect_student.txt', 'w') as f:
            sys.stdout = f
            q.sumArray(array)
        sys.stdout = original
        self.assertTrue(filecmp.cmp('redirect_corr.txt','redirect_student.txt',False),"Affichez-vous le contenu du tableau à l’écran? (un element par ligne)")

if __name__ == '__main__':
    unittest.main()
