#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import q
from Merge import *
import random as rd 
rd.seed(2019)

#Correct solution


class TestPageRank(unittest.TestCase):

	def test_exist_arrToMat(self):
		self.assertTrue(hasattr(q, 'merge'), "@1@: " + _("You did not name the method as expected."))

	def test_merge_1(self):
		#test len(tab1)<len(tab2)
		tab1=[rd.randint(1,100) for i in range(13)]
		tab2=[rd.randint(1,100) for i in range(37)]
		ans=merge(tab1,tab2) 
		student=q.merge(tab1,tab2)
		for i in range(len(ans)):
			for j in range(len(ans)):
				self.assertEqual(ans[i],student[i],"@1@: Il y a un problème dans la fonction merge()")

	def test_merge_2(self):
		#test len(tab1)>len(tab2)
		tab1=[rd.randint(1,100) for i in range(37)]
		tab2=[rd.randint(1,100) for i in range(13)]
		ans=merge(tab1,tab2) 
		student=q.merge(tab1,tab2)
		for i in range(len(ans)):
			for j in range(len(ans)):
				self.assertEqual(ans[i],student[i],"@1@: Il y a un problème dans la fonction merge()")

if __name__ == '__main__':
	unittest.main()
