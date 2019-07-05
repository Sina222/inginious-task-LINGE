#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import CorrQ as corr
import q


class TestGetCountry(unittest.TestCase):
    def test_exist(self):
        self.assertTrue(hasattr(q, 'maxmatrice'), _("You did not name the method as expected."))

    def test_cases(self):
        matrice1 = [[1,3,5],[2,7,3]]
        matrice2 = [[-8,-8,-10],[1,7,-8]]
        matrice3 = [[0,0,0],[0,0,0]]
        matrice4 = [[200,110,5],[2,100,3]]
        corr_ans = corr.maxmatrice(matrice1)
        stu_ans = q.maxmatrice(matrice1)
        corr_ans2 = corr.maxmatrice(matrice2)
        stu_ans2 = q.maxmatrice(matrice2)
        corr_ans3 = corr.maxmatrice(matrice3)
        stu_ans3 = q.maxmatrice(matrice3)
        corr_ans4 = corr.maxmatrice(matrice4)
        stu_ans4 = q.maxmatrice(matrice4)
        self.assertEqual(corr_ans, stu_ans)
        self.assertEqual(corr_ans2, stu_ans2)
        self.assertEqual(corr_ans3, stu_ans3)
        self.assertEqual(corr_ans4, stu_ans4)


if __name__ == '__main__':
	unittest.main()
