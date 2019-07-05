#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import q 
import Examen
import random as rd 
import sys
import filecmp
rd.seed(2019)

class TestExamen(unittest.TestCase):

	def test_exist_examen(self):
		self.assertTrue(hasattr(q, 'examen'), "@1@: " + _("You did not name the method as expected."))
	
	def test_print(self):
		L=[rd.randint(1,100) for i in range(30)]
		original = sys.stdout
		with open('redirect_corr.txt', 'w') as f:
			sys.stdout = f
			Examen.launch(L) 
		with open('redirect_student.txt', 'w') as f:
			sys.stdout = f
			q.launch(L)
		sys.stdout = original
		self.assertTrue(filecmp.cmp('redirect_corr.txt','redirect_student.txt',False),"Calculs erronés et/ou affichage non conforme")

if __name__ == '__main__':
	unittest.main()
