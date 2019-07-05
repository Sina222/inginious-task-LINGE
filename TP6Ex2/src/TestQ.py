#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import q
import CorrQ as corr
import random

#Creation of the random matrix M
M = [[random.randint(80,101),random.randint(0,21)] for i in range(24)]


class TestPageRank(unittest.TestCase):

	def test_exist_name(self):
		self.assertTrue(hasattr(q, 'tempete'), _("You did not name the method as expected."))

	def test(self):
		stud_ans = q.tempete(M)
		corr_ans = corr.tempete(M)
		self.assertEqual(stud_ans,corr_ans,_("You did not return the rigth result for the matrix \n M = {} \n Your result : \n ans = {} \n The expected result : \n ans = {} ").format(M,stud_ans,corr_ans))

if __name__ == '__main__':
	unittest.main()
