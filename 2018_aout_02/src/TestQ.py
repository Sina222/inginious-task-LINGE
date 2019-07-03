#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random
import math

import CorrQ as corr
import q

#####################################################
## random creation of some vector x for each pilot ##
#####################################################

#variable initialisation
nb_year = 18
max_sec = 1000
nb_circuit = random.randint(2,5)
nb_pilot = random.randint(2,10)
x = []
x_single_pilot = []
x_single_circuit = []
n = random.randint(2,nb_year)

while(x == [] ):
    #creation of the array, first dimension = time for each pilots in secondes, seconde dimensions = number of the circuit, third dimension = year of the race
    x = [[[random.randint(1,max_sec) for k in range(nb_year)] for j in range(nb_circuit)] for i in range(nb_pilot)]
    #test of egality ( guarranty of only one winner)
    corr_ans = corr.piloteLePlusRapide(x, n)
    corr_ans_1 = corr.piloteLePlusRapide(x, 1)
    corr_ans_17 = corr.piloteLePlusRapide(x, 17)
    if(corr_ans == -1 or corr_ans_1 == -1 or corr_ans_17 == -1 ):
        x = []

while(x_single_circuit == [] ):
    # cretion of the matrix x for only one circuit
    x_single_circuit = [[[random.randint(1,max_sec) for k in range(nb_year)]] for i in range(nb_pilot)]
    #test of egality ( guarranty of only one winner)
    corr_ans_single_circuit = corr.piloteLePlusRapide(x_single_circuit, n)
    if(corr_ans_single_circuit == -1):
        x_single_circuit = []




class TestExtractor(unittest.TestCase):
    def test_exist(self):
        self.assertTrue(hasattr(q, 'piloteLePlusRapide'), _("You did not name the method as expected."))

    def test_cases(self):
        # test random
        corr_ans = corr.piloteLePlusRapide(x, n)
        stu_ans = q.piloteLePlusRapide(x,n)
        self.assertEqual(corr_ans, stu_ans,"The matrix x used was {} with the number of pilots = {}, the number of circuits = {} and n = {} .".format(x,nb_pilot,nb_circuit,n))
        # test with all years
        stu_ans = q.piloteLePlusRapide(x,17)
        corr_ans = corr.piloteLePlusRapide(x, 17)
        self.assertEqual(corr_ans, stu_ans,"The matrix x used was {} with the number of pilots = {}, the number of circuits = {} and n = 17 .".format(x,nb_pilot,nb_circuit))
        # test with current year
        stu_ans = q.piloteLePlusRapide(x,1)
        corr_ans = corr.piloteLePlusRapide(x, 1)
        self.assertEqual(corr_ans, stu_ans,"The matrix x used was {} with the number of pilots = {}, the number of circuits = {} and n = 1 .".format(x,nb_pilot,nb_circuit))
        # test with only one circuit
        stu_ans = q.piloteLePlusRapide(x_single_circuit,n)
        self.assertEqual(corr_ans_single_circuit, stu_ans,"The matrix x used was {} with the number of pilots = {}, the number of circuits = 1 and n = {} .".format(x_single_circuit,nb_pilot,n))

if __name__ == '__main__':
    unittest.main()
