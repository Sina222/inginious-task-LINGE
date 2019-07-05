#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import unittest
import filecmp
from random import randint as r
import CorrQ as corr
import q

#Corner case: 2 listes vides | 1 liste plus petite que l'auteur et inversément | normal case

class TestController(unittest.TestCase):

    """Test case pour tester la methode inverse()."""

    def test_exist(self):
        if not hasattr(q, 'inverse'):
            self.fail(_("La methode 'inverse()' n´est pas définie."))

    def test_arg(self):
        try:
            q.inverse([1,2,3], [4,5,6])
        except:
            self.fail(_("La methode 'inverse()' n´est pas bien définie.(A t´elle le bon nombre d'argument ?"))

    def test_normalCase(self):
        #initialisation
        a = r(0,12)*[0]
        a0 = len(a)*[0]
        for i in range(len(a)):
            a[i] = r(0,100)
            a0[i] = a[i]
        b = len(a)*[0]
        b0 = len(b)*[0]
        for i in range(len(b)):
            b[i] = r(0,100)
            b0[i] = b[i]
        #execution + gestion du fichier-out
        #creation du resultat
        res = "A = \n"
        for i in range(len(b0)):
            res = res+str(b0[i])+" "
        res += "\n"
        res += "B = \n"
        for i in range(len(a0)):
            res = res+str(a0[i])+" "
        res = res+"\n"

        orig = sys.stdout
        with open('redirect_corr.txt', 'w') as f:
            f.write(res)

        with open('redirect_student.txt', 'w') as f:
            sys.stdout = f
            q.inverse(a, b)
        txt = ""
        with open('redirect_student.txt', 'r') as f:
            txt = f.read()
        sys.stdout = orig
        #verification
        if len(a)!=len(b0) or len(b)!=len(a0):
            self.fail(_("Votre methode 'inverse()' modifie la taille des tableaux.\n Taille initiale : "+str(len(a0))+" | Taille reçu:\n Pour a: "+str(len(a))+"\nPour b: "+str(len(b))))
        
        self.assertTrue(filecmp.cmp('redirect_corr.txt','redirect_student.txt',False),_("Votre code n'affiche pas le resultat attendu pour a = "+str(a0)+" b = "+str(b0)+" .\nAttendu:\n"+res+"Reçu:\n"+txt+"'Attention:' a la fin de chaque ligne non vide affiché, il doit y avoir un 'espace' et un 'retour à la ligne'."))
    

    def test_badCase1(self):
        #initialisation
        a = r(0,5)*[0]
        a0 = len(a)*[0]
        for i in range(len(a)):
            a[i] = r(0,100)
            a0[i] = a[i]
        b = r(6,10)*[0]
        b0 = len(b)*[0]
        for i in range(len(b)):
            b[i] = r(0,100)
            b0[i] = b[i]
        #execution + gestion fichier-out
        orig = sys.stdout
        with open('redirect_student.txt', 'w') as f:
            sys.stdout = f
            q.inverse(a, b)
        sys.stdout = orig
        #verification
        n = 0
        l = ""
        with open('redirect_student.txt', 'r') as f:
            for line in f:
                n = n+1
        if n>1:
            self.fail(_("Votre code affiche plus que 1 ligne d'erreur quand la longueur de a est inférieur à celle de b."))

        if n==0:
            self.fail(_("Votre code n´affiche pas de ligne d'erreur quand la longueur de a est inférieur à celle de b."))

    def test_badCase2(self):
        #initialisation
        b = r(0,5)*[0]
        b0 = len(b)*[0]
        for i in range(len(b)):
            b[i] = r(0,100)
            b0[i] = b[i]
        a = r(6,10)*[0]
        a0 = len(a)*[0]
        for i in range(len(a)):
            a[i] = r(0,100)
            a0[i] = a[i]
        #execution + gestion fichier-out
        orig = sys.stdout
        with open('redirect_student.txt', 'w') as f:
            sys.stdout = f
            q.inverse(a, b)
        sys.stdout = orig
        #verification
        n = 0
        with open('redirect_student.txt', 'r') as f:
            for line in f:
                n += 1
        if n>1:
            self.fail(_("Votre code affiche plus que 1 ligne d'erreur quand la longueur de b est inférieur à celle de a."))

        if n==0:
            self.fail(_("Votre code n´affiche pas de ligne d'erreur quand la longueur de b est inférieur à celle de a."))

    def test_caseEmpty(self):
        #initialisation
        a = []
        b = []
        #execution + gestion du fichier-out
        orig = sys.stdout
        res = "A = \n\nB = \n"
        with open('redirect_corr.txt', 'w') as f:
            sys.stdout = f
            corr.inverse(a, b)

        with open('redirect_student.txt', 'w') as f:
            sys.stdout = f
            q.inverse(a, b)
        #res = "A = \n\nB = \n\n"
        with open('redirect_corr.txt', 'r') as f:
            res = f.read()
        txt = ""
        with open('redirect_student.txt', 'r') as f:
            txt = f.read()
        sys.stdout = orig
        #verification
        if len(a)!=0 or len(b)!=0:
            self.fail(_("Votre methode 'inverse()' modifie la taille des tableaux.\n Tableaux finaux: a = "+str(a)+" b = "+str(b)))

        self.assertTrue(filecmp.cmp('redirect_corr.txt','redirect_student.txt',False),_("Votre code n´affiche pas le resultat attendu pour 2 tableaux vides.\nAttendu:\n"+res+"Reçu:\n"+txt+"'Attention:' a la fin de chaque ligne non vide affiché, il doit y avoir un 'espace' et un 'retour à la ligne'.\n Hint: Dans tous les cas il y aura 4 sur la sortie standard."))


if __name__ == '__main__':
    unittest.main()
