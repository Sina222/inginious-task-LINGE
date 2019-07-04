#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import q
import Ex6Supp
import random as rd 
rd.seed(2019)

#Correct solution
A=[[rd.randint(1,10) for i in range(10)] for i in range(10)]
ans=Ex6Supp.colsomme(A) 
student=q.colsomme(A) 

class TestPageRank(unittest.TestCase):

	def test_exist_colsomme(self):
		self.assertTrue(hasattr(q, 'colsomme'), "@1@: " + _("You did not name the method as expected."))

	def test_colsomme(self):
		for i in range(len(ans)):
			self.assertEqual(ans[i],student[i],"@1@: Il y a un problème dans la fonction colsomme()")

if __name__ == '__main__':
	unittest.main()
