#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import q


class TestController(unittest.TestCase):

    """Test case pour tester la methode sousChaine()."""

    def test_exist(self):
        if not hasattr(q, 'sousChaine'):
            self.fail(_("La methode 'sousChaine()' n´est pas définie."))

    def test_arg(self):
        try:
            q.sousChaine("hhsyygajjzjehhrtdy", "azerty")
        except:
            self.fail(_("Votre code relève une exception lors de l´utilisation d´une chaines de caractère normale."))
    
    def test_excep(self):
        try:
            q.sousChaine("", "")
            q.sousChaine("azerty", "")
            q.sousChaine("", "azerty")
        except:
            self.fail(_("Votre code relève une exception lors de l´utilisation de chaines de caractères vides."))

    def test_exemple(self):
        if not q.sousChaine("dcUjnfakCvfLcgah", "UCL"):
            self.fail(_("Votre code ne donne pas le bon résultat pour l´exemple x='dcUjnfakCvfLcgah' et y='UCL'\nAttendu: True  |  Reçu: False"))

        if q.sousChaine("dcLjnfUakCvfcgah", "UCL"):
            self.fail(_("Votre code ne donne pas le bon résultat pour l´exemple x='dcLjnfUakCvfcgah' et y='UCL'\nAttendu: False  |  Reçu: True"))

    def test_cases(self):
        #normal case
        if not q.sousChaine("hhsyygajjzjehhrtdy", "azerty"):
            self.fail(_("Votre code ne donne pas le bon résultat.\nAttendu: True  |  Reçu: False"))

        if q.sousChaine("hhsyygajjzjeaze", "azersdty"):
            self.fail(_("Votre code ne donne pas le bon résultat.\nAttendu: False  |  Reçu: True"))

        #Borders cases
        if q.sousChaine("hhsyyg", "azersdtyzer"):
            self.fail(_("Votre code ne donne pas le bon résultat.\nAttendu: False  |  Reçu: True"))

        if not q.sousChaine("", ""):
            self.fail(_("Votre code ne donne pas le bon résultat lors de l´utilisation de chaines de caractères vides.\nAttendu: True  |  Reçu: False"))

        if q.sousChaine("", "azerty"):
            self.fail(_("Votre code ne donne pas le bon résultat.\nAttendu: False  |  Reçu: True"))

        if not q.sousChaine("esrdtfbygnhoj", ""):
            self.fail(_("Votre code ne donne pas le bon résultat.\nAttendu: True  |  Reçu: False"))

                
    
if __name__ == '__main__':
    unittest.main()
