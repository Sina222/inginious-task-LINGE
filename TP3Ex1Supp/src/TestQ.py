#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import CorrQ as corr
import q

class TestExtractor(unittest.TestCase):
    def test_exist(self):
        self.assertTrue(hasattr(q, 'premier'), _("You did not name the method as expected."))

    def test_cases(self):
        corr_ans = corr.premier(0)
        stu_ans = q.premier(0)
        corr_ans1 = corr.premier(1)
        stu_ans1 = q.premier(1)
        corr_ans2 = corr.premier(7)
        stu_ans2 = q.premier(7)
        corr_ans3 = corr.premier(42)
        stu_ans3 = q.premier(42)
        corr_ans4 = corr.premier(97)
        stu_ans4 = q.premier(97)
        corr_ans5 = corr.premier(99)
        stu_ans5 = q.premier(99)
        self.assertEqual(corr_ans, stu_ans, "0 n'est pas sencé être premier !")
        self.assertEqual(corr_ans1, stu_ans1, "1 est un nombre premier")
        self.assertEqual(corr_ans2, stu_ans2, "Votre code ne renvoit pas la bonne valeur pour n = 7")
        self.assertEqual(corr_ans3, stu_ans3, "Votre code ne renvoit pas la bonne valeur pour n = 42")
        self.assertEqual(corr_ans4, stu_ans4, "Votre code ne revoit pas la bonne valeur pour n = 97")
        self.assertEqual(corr_ans5, stu_ans5, "Votre code ne renvoit pas la bonne valeur pour n = 99")

if __name__ == '__main__':
    unittest.main()
