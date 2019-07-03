#!/usr/bin/python3
# -*- coding: utf-8 -*-

from CorrQ import Reveil
import unittest
import random
import q


class TestController(unittest.TestCase):

    """Test case pour tester la class Reveil."""

    def test_class(self):
        if not hasattr(q, 'Reveil'):
            self.fail(
                _("La classe n´est pas nommé correctement ou n´existe pas."))

        randSec = random.randint(0, 59)
        randMin = random.randint(0, 59)
        randHeu = random.randint(0, 23)
        const = "Reveil("+str(randHeu)+", "+str(randMin)+", "+str(randSec)+")"

        try:
            obj = q.Reveil(randHeu, randMin, randSec)
        except:
            self.fail(_("Le constructeur '__init__' n´est pas correctement implémenté.\n(A t´il les bons arguments ? Le bon nom ? initialise t'il bien les 3 variables ?)"))

        # test Seconde
        try:
            s = obj.getSeconde()
            if s != randSec:
                self.fail(_("Le nombre de seconde n´est pas correctement initialisé.\nTest avec: " +
                            str(const)+"; Attendu: "+str(randSec)+"  Reçu: "+str(s)))
        except:
            self.fail(_("La methode 'getSeconde' n´est pas correctement implémenté.\n(A t´il le bon nom ? Le(s) bon(s) argument(s) ? La variable 'seconde' a correctement été initialisée ?)"))

        # test Minute
        try:
            m = obj.getMinute()
            if m != randMin:
                self.fail(_("Le nombre de minute n´est pas correctement initialisé.\nTest avec: " +
                            str(const)+"; Attendu: "+str(randMin)+"  Reçu: "+str(m)))
        except:
            self.fail(_("La methode 'getMinute' n´est pas correctement implémenté.\n(A t´il le bon nom ? Le(s) bon(s) argument(s) ? La variable 'minute' a correctement été initialisée ?)"))

        # test Heure
        try:
            h = obj.getHeure()
            if h != randHeu:
                self.fail(_("Le nombre d´heure n´est pas correctement initialisé.\nTest avec: " +
                            str(const)+"; Attendu: "+str(randHeu)+"  Reçu: "+str(h)))
        except:
            self.fail(_("La methode 'getHeure' n´est pas correctement implémenté.\n(A t´il le bon nom ? Le(s) bon(s) argument(s) ? La variable 'heure' a correctement été initialisée ?)"))

    def test_exist(self):
        if not hasattr(q.Reveil, 'nouvelleHeure'):
            self.fail(_("La methode 'nouvelleHeure()' n´est pas définie."))

    def test_cases(self):
        randSec = random.randint(0, 59)
        randMin = random.randint(0, 59)
        randHeu = random.randint(0, 23)
        obj1 = q.Reveil(1, 20, 59)
        obj1b = Reveil(1, 20, 59)
        obj2 = q.Reveil(1, 50, 20)
        obj2b = Reveil(1, 50, 20)
        obj3 = q.Reveil(23, 20, 20)
        obj3b = Reveil(23, 20, 20)
        objRand = q.Reveil(randHeu, randMin, randSec)
        objRandb = Reveil(randHeu, randMin, randSec)

        n1 = random.randint(1, 59)
        obj1.nouvelleHeure(n1)
        obj1b.nouvelleHeure(n1)
        if not(obj1.getSeconde() == obj1b.getSeconde() and obj1.getMinute() == obj1b.getMinute() and obj1.getHeure() == obj1b.getHeure()):
            self.fail(_("Votre méthode 'nouvelleHeure' n´est pas implémenté correctement.\nPour: Reveil(heure={}, minute={}, seconde={}).nouvelleHeure({})\nAttendu: Reveil(heure={}, minute={}, seconde={})  |  Reçu: Reveil(heure={}, minute={}, seconde={})".format(
                1, 20, 59, n1, obj1b.getHeure(), obj1b.getMinute(), obj1b.getSeconde(), obj1.getHeure(), obj1.getMinute(), obj1.getSeconde())))

        n2 = random.randint(600, 4140)
        obj2.nouvelleHeure(n2)
        obj2b.nouvelleHeure(n2)
        if not(obj2.getSeconde() == obj2b.getSeconde() and obj2.getMinute() == obj2b.getMinute() and obj2.getHeure() == obj2b.getHeure()):
            self.fail(_("Votre méthode 'nouvelleHeure' n´est pas implémenté correctement.\nPour: Reveil(heure={}, minute={}, seconde={}).nouvelleHeure({})\nAttendu: Reveil(heure={}, minute={}, seconde={})  |  Reçu: Reveil(heure={}, minute={}, seconde={})".format(
                1, 50, 20, n2, obj2b.getHeure(), obj2b.getMinute(), obj2b.getSeconde(), obj2.getHeure(), obj2.getMinute(), obj2.getSeconde())))

        n3 = random.randint(3600, 6000)
        obj3.nouvelleHeure(n3)
        obj3b.nouvelleHeure(n3)
        if not(obj3.getSeconde() == obj3b.getSeconde() and obj3.getMinute() == obj3b.getMinute() and obj3.getHeure() == obj3b.getHeure()):
            self.fail(_("|Attention, passé 23 heures, le nombre d´heures revient à 0.|\nVotre méthode 'nouvelleHeure' n´est pas implémenté correctement.\nPour: Reveil(heure={}, minute={}, seconde={}).nouvelleHeure({})\nAttendu: Reveil(heure={}, minute={}, seconde={})  |  Reçu: Reveil(heure={}, minute={}, seconde={})".format(
                23, 20, 20, n3, obj3b.getHeure(), obj3b.getMinute(), obj3b.getSeconde(), obj3.getHeure(), obj3.getMinute(), obj3.getSeconde())))

        nRand = random.randint(0, 3600)
        objRand.nouvelleHeure(nRand)
        objRandb.nouvelleHeure(nRand)
        if not(objRand.getSeconde() == objRandb.getSeconde() and objRand.getMinute() == objRandb.getMinute() and objRand.getHeure() == objRandb.getHeure()):
            self.fail(_("Votre méthode 'nouvelleHeure' n´est pas implémenté correctement.\nPour: Reveil(heure={}, minute={}, seconde={}).nouvelleHeure({})\nAttendu: Reveil(heure={}, minute={}, seconde={})  |  Reçu: Reveil(heure={}, minute={}, seconde={})".format(
                randHeu, randMin, randSec, nRand, objRandb.getHeure(), objRandb.getMinute(), objRandb.getSeconde(), objRand.getHeure(), objRand.getMinute(), objRand.getSeconde())))

        r = random.randint(1, 7)
        h1 = obj1.getHeure()
        m1 = obj1.getMinute()
        s1 = obj1.getSeconde()
        obj1.nouvelleHeure(0)
        if not(obj1.getSeconde() == s1 and obj1.getMinute() == m1 and obj1.getHeure() == h1):
            self.fail(
                _("Attention votre code change le réveil quand on ajoute 0 seconde !! (Il ne devrai pas changer)"))

        obj1.nouvelleHeure(86400*r)
        if not(obj1.getSeconde() == s1 and obj1.getMinute() == m1 and obj1.getHeure() == h1):
            self.fail(
                _("Attention votre code change le réveil quand on ajoute des jours entiers ! (Ll ne devrai pas changer)"))


if __name__ == '__main__':
    unittest.main()
