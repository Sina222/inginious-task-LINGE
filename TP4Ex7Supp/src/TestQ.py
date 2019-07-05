#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random
import sys
import filecmp

import q

CORRECT_EMPTY = ([[], "Guy"],"empty", "Votre programme n'affiche pas la bonne liste si la liste initiale est vide'")
CORRECT_SAME = ([["Ameline","Jean","Luc"],"Luc"],"same","Votre programme n'affiche pas la bonne liste si le prénom est déjà dedans")
CORRECT_END = ([["Ameline","Jean","Luc"],"Lucas"], "end", "Votre programme ne retourne pas la bonne somme pour une liste avec le prenom s'ajoutant à la fin")
CORRECT_BEGIN = ([["Ameline","Jean","Luc"],"Alois"], "begin", "Votre programme ne retourne pas la bonne somme pour une liste avec le prenom s'ajoutant au début")
CORRECT_BETWEEN = ([["Ameline","Jean","Luc"],"Guy"], "between", "Votre programme ne retourne pas la bonne somme pour une liste avec le prenom s'ajoutant au milieu")

TESTS = [CORRECT_EMPTY,CORRECT_SAME,CORRECT_END,CORRECT_BETWEEN]


class TestExtractor(unittest.TestCase):
    def test_exist(self):
        self.assertTrue(hasattr(q, 'ajoutPrenom'), ("You did not name the method as expected."))

    def test_cases(self):
        for t in TESTS:
            #original = sys.stdout
            ans = t[2]
            corr_ans = t[1]
            with open('redirect_student.txt', 'w') as f:
                sys.stdout = f
                q.ajoutPrenom(t[0][0],t[0][1])
            # sys.stdout = original
            self.assertTrue(filecmp.cmp(corr_ans,'redirect_student.txt',False),ans)

if __name__ == '__main__':
    unittest.main()
