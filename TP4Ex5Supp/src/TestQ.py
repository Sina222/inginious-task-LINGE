#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import q
import CorrQ
import random as rd 
rd.seed(2019)

#Correct solution
A=[[rd.randint(1,10) for i in range(10)] for i in range(10)]
ans=CorrQ.ligsomme(A) 
student=q.ligsomme(A) 

class TestLigSomme(unittest.TestCase):

	def test_exist_ligsomme(self):
		self.assertTrue(hasattr(q, 'ligsomme'), _("You did not name the method as expected."))

	def test_ligsomme(self):
		for i in range(len(ans)):
			self.assertEqual(ans[i],student[i]," Il y a un problème dans la fonction ligsomme()")

if __name__ == '__main__':
	unittest.main()
