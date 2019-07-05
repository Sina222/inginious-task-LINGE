#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random
import math

import CorrQ as corr
import q

#matrix test case
valid_3 = ([[1,1,1],[5,2,1],[2,3,4]],_("You did not pass the test for a 3x3 matrix."))
valid_4 = ([[1,1,1,1],[1,1,1,2],[2,3,4,4],[2,3,3,4]],_("You did not pass the test for a matrix bigger than 3x3."))
not_square_but_sum = ([[1,1,1],[4,5,6]],_("You did not pass the test for a non square matrix."))
not_diagonal = ([[1,1,1,1],[1,1,1,2],[1,2,3,4],[3,4,2,2]],_("You did not test the diagonales."))
not_valid = ([[1,1,1,1],[5,2,1,1],[2,3,4,1],[1,1,1,1]],_("Your test accept non antimagic matrix."))

tests = [valid_3,valid_4,not_square_but_sum,not_diagonal,not_valid]

class TestExtractor(unittest.TestCase):
    def test_exist(self):
        self.assertTrue(hasattr(q, 'estAntiMagique'), _("You did not name the method as expected."))

    def test_cases(self):
        for test in tests :
            corr_ans =  corr. estAntiMagique(test[0])
            stu_ans = q. estAntiMagique(test[0])
            self.assertEqual(corr_ans, stu_ans,test[1])

if __name__ == '__main__':
    unittest.main()
