#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import CorrQ as corr
import q

class TestExtractor(unittest.TestCase):
    def test_exist(self):
        self.assertTrue(hasattr(q, 'arret'), _("You did not name the method as expected."))

    def test_cases(self):
        for nb_test in range(0,6):
            H = random.randint(1,30)
            L = random.randint(1,30)
            BUT = [['X' for j in range(0,L)] for i in range(0,H)]
            G = [random.randrange(H-1), random.randrange(L-1)]
            B = [random.randrange(H-1), random.randrange(L-1)]
            BUT[G[0]][G[1]] = 'G'
            BUT[B[0]][B[1]] = 'B'
            corr_ans = corr.arret(BUT)
            stu_ans = q.arret(BUT)
            error_message = "La bonne réponse avec G en [{}][{}] et B en [{}][{}] est la direction {} avec un angle de {} sur une distance de {}"
            self.assertEqual(corr_ans, stu_ans, error_message.format(G[0],G[1],B[0],B[1],corr_ans[0],corr_ans[1],corr_ans[2]))
    
    def test_same(self):
        H = 5
        L = 10
        BUT = [['X' for j in range(0,L)] for i in range(0,H)]
        G = [1, 3]
        B = [3, 3]
        BUT[G[0]][G[1]] = 'G'
        BUT[B[0]][B[1]] = 'B'
        corr_ans = corr.arret(BUT)
        stu_ans = q.arret(BUT)
        error_message = "La bonne réponse avec G en [{}][{}] et B en [{}][{}] est la direction {} avec un angle de {} sur une distance de {}"
        self.assertEqual(corr_ans, stu_ans, error_message.format(G[0],G[1],B[0],B[1],corr_ans[0],corr_ans[1],corr_ans[2]))


if __name__ == '__main__':
    unittest.main()
