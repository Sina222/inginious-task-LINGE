#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import q
from Ex3 import *
import random as rd 
rd.seed(2019)

#Correct solution


class TestPageRank(unittest.TestCase):

	def test_exist_volume(self):
		self.assertTrue(hasattr(q, 'volume'), "@1@: " + _("You did not name the method as expected."))

	def test_exist_surface(self):
		self.assertTrue(hasattr(q, 'surface'), "@2@: " + _("You did not name the method as expected."))

	def test_volume(self):
		val=[rd.randint(1,100) for i in range(10)]
		for i in val:
			self.assertEqual(volume(i),q.volume(i),"@1@: Il y a un problème dans la fonction volume()")

	def test_surface(self):
		val=[rd.randint(1,100) for i in range(10)]
		for i in val:
			self.assertEqual(surface(i),q.surface(i),"@2@: Il y a un problème dans la fonction surface()")

if __name__ == '__main__':
	unittest.main()
