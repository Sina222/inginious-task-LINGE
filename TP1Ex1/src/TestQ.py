#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import unittest
import filecmp
from random import randint as r
import CorrQ as corr
import q

class TestController(unittest.TestCase):

    """Test case pour tester la methode inverse()."""

    def test_exist(self):
        if not hasattr(q, 'heure'):
            self.fail(_("La methode 'heure()' n´est pas définie."))

    def test_arg(self):
        try:
            q.heure(42)
        except:
            self.fail(_("La methode 'heure()' n´est pas correctement définie.(A t´elle le bon nombre d´argument ?)"))

    def test_random(self):
        for i in range(5): #make 5 tests
            original = sys.stdout
            rand = r(0, 86400)
            with open('redirect_corr.txt', 'w') as f:
                sys.stdout = f
                corr.heure(rand)
            with open('redirect_corr.txt', 'r') as f:
                res = f.read()
        
            with open('redirect_student.txt', 'w') as f:
                sys.stdout = f
                q.heure(rand)
            with open('redirect_student.txt', 'r') as f:
                txt = f.read()

            sys.stdout = original

            if not filecmp.cmp('redirect_corr.txt','redirect_student.txt',False):
                self.fail(_("Votre programme n´affiche pas le bon texte pour {}\nAttendu:\n{}\n  Reçu:\n{}".format(rand, res, txt)))

    def test_zero(self):
        original = sys.stdout
        with open('redirect_corr.txt', 'w') as f:
            sys.stdout = f
            corr.heure(0)
        with open('redirect_corr.txt', 'r') as f:
            res = f.read()
    
        with open('redirect_student.txt', 'w') as f:
            sys.stdout = f
            q.heure(0)
        with open('redirect_student.txt', 'r') as f:
            txt = f.read()

        sys.stdout = original

        if not filecmp.cmp('redirect_corr.txt','redirect_student.txt',False):
            self.fail(_("Votre programme n´affiche pas le bon texte pour {}\nAttendu:\n{}\nReçu:\n{}".format(0, res, txt)))
        

if __name__ == '__main__':
    unittest.main()
