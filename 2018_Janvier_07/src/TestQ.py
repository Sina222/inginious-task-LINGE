#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random
import math

import CorrQ as corr
import q

#random creation of the matrix M and the price P
x = random.randint(0,20) #range for abs pos
y = random.randint(0,20) #range for ordo pos
nb_run = random.randint(5,15)
M = [[i,random.randint(-x,x),random.randint(-y,y),random.randint(-x,x),random.randint(-y,y)] for i in range(1,nb_run)]
P = random.randint(5,20)


class TestExtractor(unittest.TestCase):
    def test_exist(self):
        self.assertTrue(hasattr(q, 'PayeTaxi'), _("You did not name the method as expected."))

    def test_cases(self):
        # test for a random day
        corr_ans =  corr.PayeTaxi(M,P)
        stu_ans = q.PayeTaxi(M,P)
        self.assertEqual(corr_ans, stu_ans,_("The matrix used was M = {} and the price was P = {} .").format(M,P))
        # test for an empty day
        corr_ans =  corr.PayeTaxi([],0)
        stu_ans = q.PayeTaxi([],0)
        self.assertEqual(corr_ans, stu_ans,_("The empty case was not tested, it should return {}").format(corr_ans))


if __name__ == '__main__':
    unittest.main()
