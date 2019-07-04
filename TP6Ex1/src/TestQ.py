#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import q
from inverse import *
import random as rd 
rd.seed(2019)

#Correct solution
L=[rd.randint(1,100) for i in range(20)]
ans=inverse(L) 
student=q.inverse(L) 

class TestPageRank(unittest.TestCase):

	def test_exist_inverse(self):
		self.assertTrue(hasattr(q, 'inverse'), "@1@: " + _("You did not name the method as expected."))

	def test_inverse(self):
		for i in range(len(ans)):
			self.assertEqual(ans[i],student[i],"@1@: Il y a un problème dans la fonction inverse()")

if __name__ == '__main__':
	unittest.main()
