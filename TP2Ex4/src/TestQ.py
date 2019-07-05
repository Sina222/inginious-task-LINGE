#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import q
from Ex4 import *
import random as rd 
rd.seed(2019)

#Correct solution


class TestPrix(unittest.TestCase):

	def test_exist_prix(self):
		self.assertTrue(hasattr(q, 'prix'), "@1@: " + _("You did not name the method as expected."))

	def test_prix(self):
		val=[(rd.randint(1,100),rd.randint(1,100)) for i in range(20)]
		val.append((3,3))
		val.append((0,0))
		val.append((3,5))
		for i in val:
			self.assertEqual(prix(i[0],i[1]),q.prix(i[0],i[1]),"@1@: Il y a un problème dans la fonction prix()")

if __name__ == '__main__':
	unittest.main()
