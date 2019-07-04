#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import CorrQ as corr
import q


CORRECT_ONE = ([[[1],[1]],[[2],[1]]], 1, "Gerez vous le cas de l'as?")
CORRECT_SAME = ([[[10],[1]],[[10],[2]]], 1,"Gerez vous le cas avec deux cartes de la même valeur?")
CORRECT_RANDOM = ([
    [[9, 10, 5],[2, 4, 2]],
    [[10, 11, 11],[2, 3, 2]]], 
    2,"Votre programme ne retourne pas le bon gagnant")


TESTS = [CORRECT_ONE, CORRECT_SAME,CORRECT_RANDOM]


class TestExtractor(unittest.TestCase):
    def test_exist(self):
        self.assertTrue(hasattr(q, 'bataille'), ("You did not name the method as expected."))

    def test_corner_cases(self):
        for t in TESTS:
            ans = t[2]
            corr_ans = t[1]
            stu_ans = q.bataille(t[0][0], t[0][1])
            self.assertEqual(corr_ans, stu_ans, ans)


if __name__ == '__main__':
    unittest.main()
