#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import q
import CorrQ as corr
import random
from unittest.mock import patch
import sys

#Creation of the random number for the test
a_pos = random.randint(0,100)
b_pos = random.randint(0,100)
c_pos = random.randint(0,100)
max_pos = random.randint(100,150)
a_neg = random.randint(-100,-50)
b_neg = random.randint(-100,-50)
c_neg = random.randint(-100,-50)
max_neg = random.randint(-50,0)
test_pos = [a_pos,b_pos,c_pos]
test_pos_rev = [c_pos,b_pos,a_pos]
test_neg = [a_neg,b_neg,c_neg]
test_neg_rev = [c_neg,b_neg,a_neg]
test_neg_pos = [c_neg,b_pos,a_neg]
test_eq2_pos = [max_pos,c_pos,max_pos]
test_eq2_neg = [c_neg,max_neg,max_neg]
test_eq2_pos_neg = [max_pos,max_pos,max_neg]
test_eq3 = [max_pos,max_pos,max_pos]

original = sys.stdout

TEST = [test_pos,test_neg,test_pos_rev,test_neg_pos,test_neg_rev,test_eq2_neg,test_eq2_pos,test_eq2_pos_neg,test_eq3]


class TestPageRank(unittest.TestCase):

	def test_exist_name(self):
		self.assertTrue(hasattr(q, 'main'), _("You did not have a main methode."))

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
			self.assertEqual(correct, stud,_("Your output don't match the expected one for the entries : \n a = {} \n b = {} \n c = {}\n The expected output :\n {} \n Your output:\n {}").format(test[0],test[1],test[2],correct,stud))
			corr_ans.close()
			stu_ans.close()

if __name__ == '__main__':
	unittest.main()
