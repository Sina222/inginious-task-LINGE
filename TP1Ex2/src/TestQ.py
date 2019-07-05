#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import q
import CorrQ as corr
import random
from unittest.mock import patch
import sys

#Creation of the random number for the test
a_pos = random.randint(0,10)
b_pos = random.randint(0,10)
a_neg = random.randint(-10,0)
b_neg = random.randint(-10,0)
test_pos = [a_pos,b_pos]
test_neg = [a_neg,b_neg]
test_pos_neg = [a_pos,b_neg]

original = sys.stdout

TEST = [test_pos,test_neg,test_pos_neg]


class TestPageRank(unittest.TestCase):

	def test_exist_name(self):
		self.assertTrue(hasattr(q, 'main'), _("You did not have a main methode."))
		self.assertTrue(hasattr(q, 'moyenne'), _("You did not have a moyenne methode."))

	def test(self):
		for test in TEST :
			stu_ans = open("stu_ans.txt", 'w')
			sys.stdout = stu_ans
			with patch('builtins.input', side_effect=test):
				q.main()
			stu_ans.close()
			corr_ans = open("corr_ans.txt", 'w')
			sys.stdout = corr_ans
			with patch('builtins.input', side_effect=test):
				corr.main()
			corr_ans.close()
			corr_ans = open("corr_ans.txt", 'r')
			correct = corr_ans.read()
			stu_ans = open("stu_ans.txt", 'r')
			stud = stu_ans.read()
			self.assertEqual(correct, stud,_("Your output don't match the expected one for the entries : \n a = {} \n b = {} \n The expected output :\n {} \n Your output:\n {}").format(test[0],test[1],correct,stud))
			corr_ans.close()
			stu_ans.close()

if __name__ == '__main__':
	unittest.main()
