#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import q
import CorrQ
import random as rd 
rd.seed(2019)

#Correct solution
A=[[rd.randint(1,10) for i in range(10)] for i in range(10)]
ans=CorrQ.colsomme(A) 
student=q.colsomme(A) 

class TestColSomme(unittest.TestCase):

	def test_exist_colsomme(self):
		self.assertTrue(hasattr(q, 'colsomme'), _("You did not name the method as expected."))

	def test_colsomme(self):
		for i in range(len(ans)):
			self.assertEqual(ans[i],student[i],"Il y a un problème dans la fonction colsomme()")

if __name__ == '__main__':
	unittest.main()
