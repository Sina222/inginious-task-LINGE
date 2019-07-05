#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
from unittest.mock import patch

import random
import sys
import filecmp

import CorrQ as corr
import q


CORRECT_EMPTY = ([-1], "output_empty", "Votre programme affiche quelque chose quand l'input est directement -1")
CORRECT_SAME = ([2,2,2,2,2,2,-1], "output_same","Votre programme n'affiche pas le bon texte si il y a seulement un chiffre plusieurs fois")

TESTS = [CORRECT_EMPTY, CORRECT_SAME]

class TestFileReading(unittest.TestCase):
    def test_exist(self):
        self.assertTrue(hasattr(q, 'compte'), ("You did not name the method as expected."))

    def test_cases(self):
        for t in TESTS:
            ans = t[2]
            corr_ans = t[1]
            user_input = t[0]
            original = sys.stdout
            with patch('builtins.input', side_effect=user_input):
                with open('redirect_student.txt', 'w') as f:
                    sys.stdout = f
                    q.compte()  
            sys.stdout = original
            self.assertTrue(filecmp.cmp('redirect_student.txt',corr_ans,False), ans)

    def test_random(self):
        for i in range(5): #make 5 tests
            user_input = []
            for i in range(10): #list of size 10
                user_input.append(random.randint(0,9))
            user_input.append(-1)

            original = sys.stdout
            with patch('builtins.input', side_effect=user_input):
                with open('redirect_corr.txt', 'w') as f:
                    sys.stdout = f
                    corr.compte()
            
            with patch('builtins.input', side_effect=user_input):
                with open('redirect_student.txt', 'w') as f:
                    sys.stdout = f
                    q.compte()
            sys.stdout = original

            self.assertTrue(filecmp.cmp('redirect_corr.txt','redirect_student.txt',False),"Votre programme n'affiche pas le bon texte pour {}".format(user_input))



if __name__ == '__main__':
    unittest.main()
