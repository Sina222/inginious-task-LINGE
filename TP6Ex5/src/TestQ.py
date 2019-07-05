#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import q
from ArrToMat import *
import random as rd 
rd.seed(2019)

#Correct solution
L=[[rd.randint(1,100) for j in range(10)] for i in range(10)]
ans=arrToMat(L) 
student=q.arrToMat(L) 

class TestPageRank(unittest.TestCase):

	def test_exist_arrToMat(self):
		self.assertTrue(hasattr(q, 'arrToMat'), "@1@: " + _("You did not name the method as expected."))

	def test_arrToMat(self):
		for i in range(len(ans)):
			for j in range(len(ans)):
				self.assertEqual(ans[i][j],student[i][j],"@1@: Il y a un problème dans la fonction arrToMat()")

if __name__ == '__main__':
	unittest.main()
