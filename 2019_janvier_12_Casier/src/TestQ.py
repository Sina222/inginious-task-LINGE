#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
from q import Casier as CasierStudent

from Casier import *
from Biere import *
import random as rd 
rd.seed(2019)

nom_biere=["Jupiler","leffe","Chimay"]

def generateCasier(min_value,max_value):
    instances=[[] for i in range(5)]
    for i in range(5):
        temp=[]
        for j in range(10):
            biere_=rd.choice(nom_biere)
            alcool_=rd.uniform(min_value, max_value)
            temp.append(Biere(biere_,alcool_))
        instances[i]=temp
    return instances

class TestCasier(unittest.TestCase):

	def test_exist_init(self):
		self.assertTrue(hasattr(CasierStudent, '__init__'), "@1@: " + _("You did not name the method as expected."))

	def test_exist_party(self):
		self.assertTrue(hasattr(CasierStudent, 'party'), "@2@: " + _("You did not name the method as expected."))

	def test_exist_directories(self):
		self.assertTrue(hasattr(CasierStudent, 'avgAlcool'), "@3@: " + _("You did not name the method as expected."))

	def test_exist_subfiles(self):
		self.assertTrue(hasattr(CasierStudent, 'isStronger'), "@4@: " + _("You did not name the method as expected."))
	def test_party(self):
		"""
		Une fonction party(name) permettant de parcourir le casier et d’en boire toutes 
		les bières portant le nom fourni en argument par l’utilisateur (seules les bières pleines peuvent être bues):
		"""
		casier_stu=CasierStudent(generateCasier(1.5,5))
		test_nom_bierre=casier_stu.getBac()[0][1].getNom()
		casier_stu.party(test_nom_bierre)
		currentBac=casier_stu.getBac()
		for i in range(len(currentBac)):
			for j in range(len(currentBac[0])):
				if currentBac[i][j].getNom()==test_nom_bierre:
					self.assertFalse(currentBac[i][j].estPleine(),"@1@: Il y a un problème dans la fonction party()")

	def test_avgAlcool(self):
		"""
		Une fonction avgAlcool() permettant de calculer le taux moyen d’alcool contenu dans les bières (pleines) du casier.
		Si le casier ne contient que des bières vides, votre fonction doit renvoyer zéro:
		"""
		inst=generateCasier(1.5,5)
		casier_ans=Casier(inst)
		casier_stu=CasierStudent(inst)
		self.assertEqual(casier_ans.avgAlcool(),casier_stu.avgAlcool(),"@2@: Il ya un problème dans la fonction avgAlcool()")

	def test_isStronger(self):
		"""
		Une fonction isStronger(tableau) qui renverra true si le casier sur lequel est appliqué la fonction 
		possède un taux d’alcool moyen ( avgAlcool ) strictement supérieur à tous les autres casiers fournis
		 en argument dans un tableau, et false sinon:
		"""
		temp=[]
		GenCasier=[[] for i in range(3)]   
		temp.append(Casier(generateCasier(0,1)))
		temp.append(Casier(generateCasier(1,1.5)))
		GenCasier[0]=temp
		temp=[]
		temp.append(Casier(generateCasier(3.5,6)))
		temp.append(Casier(generateCasier(10,10)))
		GenCasier[1]=temp
		temp=[]
		temp.append(Casier(generateCasier(0,0)))
		GenCasier[2]=temp
		RepSup=['True','False','True']
		casier_stu=CasierStudent(generateCasier(5,5))

		self.assertTrue(casier_stu.isStronger(GenCasier[0]), "@3@: Il y a un problème dans la fonction isStronger()")
		self.assertFalse(casier_stu.isStronger(GenCasier[1]), "@3@: Il y a un problème dans la fonction isStronger()")
		self.assertTrue(casier_stu.isStronger(GenCasier[2]), "@3@: Il y a un problème dans la fonction isStronger()")

if __name__ == '__main__':
	unittest.main()
