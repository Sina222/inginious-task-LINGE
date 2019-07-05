#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import unittest
import CorrQ as corr
import q

class TestController(unittest.TestCase):

    """Test case pour tester la methode change() -> remplace 'r' to 'l'."""

    def test_exist(self):
        if not hasattr(q, 'change'):
            self.fail("@1@: " + _("La methode 'change()' n´est pas définie."))

    def test_arg(self):
        try:
            q.change("azerty")
        except:
            self.fail("@1@: " + _("La methode 'change()' n´est pas correctement définie.(A t´elle le bon nombre d´argument ?)"))

    def test_normal(self):
        string = "Un autre prodige parut ensuite dans le ciel ; un grand dragon roux, qui avait sept têtes et dix cornes, et sept diadèmes sur ses sept têtes."
        res = "Un autle plodige palut ensuite dans le ciel ; un gland dlagon loux, qui avait sept têtes et dix colnes, et sept diadèmes sul ses sept têtes."
        student = q.change(string)
        if student!=res:
            self.fail("@1@: " + _("Votre code ne donne pas le résultat attendu avec la chaine de caratère suivante:\n'{}'\nAttendu:\n'{}'\nReçu:\n'{}'").format(string, res, student))
        
        string = "Mais ceux-ci furent les plus faibles ; et depuis ce temps-là ils ne parurent plus dans le ciel."
        res = "Mais ceux-ci fulent les plus faibles ; et depuis ce temps-là ils ne palulent plus dans le ciel."
        student = q.change(string)
        if student!=res:
            self.fail("@1@: " + _("Votre code ne fonctionne pas correctement. Veillez bien à changer les caractères 'r' par 'l'."))
        

if __name__ == '__main__':
    unittest.main()
