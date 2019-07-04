#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
from q import PageRank as PageRankStudent

from PageRank import *
import random as rd 
rd.seed(2019)

#Correct solution
PageRank_correct=PageRank()
A=[[rd.randint(1,10) for i in range(5)] for i in range(5)]
P_correct=PageRank_correct.ProbabilityMatrix(A) #test 1

score = PageRank_correct.IndegreeVector(A)
prod_Mat_Vec_correct=PageRank_correct.produitMatriceVecteur(A,score) #test 2

PR_score_correct=PageRank_correct.PageRankScore(A) #test 3

class TestPageRank(unittest.TestCase):

	def test_exist_ProbMatrix(self):
		self.assertTrue(hasattr(PageRankStudent, 'ProbabilityMatrix'), "@1@: " + _("You did not name the method as expected."))

	def test_exist_Product(self):
		self.assertTrue(hasattr(PageRankStudent, 'produitMatriceVecteur'), "@2@: " + _("You did not name the method as expected."))

	def test_exist_PageRank(self):
		self.assertTrue(hasattr(PageRankStudent, 'PageRankScore'), "@3@: " + _("You did not name the method as expected."))

	def test_ProbMatrix(self):
		PageRank_stu=PageRankStudent()
		Proba_stu=PageRank_stu.ProbabilityMatrix(A)
		for i in range(len(P_correct)):
			for j in range(len(P_correct[0])):
				self.assertEqual(P_correct[i][j],Proba_stu[i][j],"@1@: Il y a un problème dans la fonction ProbabilityMatrix()")

	def test_Product(self):
		PageRank_stu=PageRankStudent()
		score = PageRank_stu.IndegreeVector(A)
		prod_stu=PageRank_stu.produitMatriceVecteur(A,score) #test 2
		for i in range(len(prod_Mat_Vec_correct)):
			self.assertEqual(prod_Mat_Vec_correct[i],prod_stu[i],"@2@: Il y a un problème dans la fonction produitMatriceVecteur()")

	def test_PageRank(self):
		PageRank_stu=PageRankStudent()
		PR_score_stu=PageRank_stu.PageRankScore(A)
		for i in range(len(PR_score_correct)):
			self.assertEqual(PR_score_correct[i],PR_score_stu[i],"@3@: Il y a un problème dans la fonction PageRankScore()")

if __name__ == '__main__':
	unittest.main()
