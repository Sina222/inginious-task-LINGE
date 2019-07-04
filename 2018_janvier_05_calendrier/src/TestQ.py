#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import CorrQ as corr
import q


DATES_INPUT = [
    {"jour": 14, "mois": 7, "annee": 1789},
    {"jour": 1, "mois": 8, "annee": 2019},
    {"jour": 1, "mois": 7, "annee": 2019},
    {"jour": 1, "mois": 3, "annee": 2019},
    {"jour": 1, "mois": 3, "annee": 2020},
    {"jour": 1, "mois": 1, "annee": 2000}
]


class TestDate(unittest.TestCase):
    def test_specs(self):
        self.assertTrue(hasattr(q, 'Date') and hasattr(q.Date, 'hier') and callable(
            q.Date.hier), _("Vous n'avez pas bien spécifié vos fonctions / votre classe."))

        self.assertTrue(hasattr(q.Date, 'getJour') and callable(q.Date.getJour) and hasattr(
            q.Date, 'getMois') and callable(q.Date.getMois) and hasattr(q.Date, 'getAnnee') and callable(q.Date.getAnnee),
            _("Vous n'avez pas bien spécifié vos fonctions / votre classe."))

        try:
            date = q.Date(24, 12, 2042)
        except TypeError:
            self.fail(
                _("Vous n'avez pas bien spécifié vos fonctions / votre classe."))

        self.assertTrue(hasattr(date, '_Date__jour') and hasattr(date, '_Date__mois') and hasattr(date, '_Date__annee'), _(
            "Vous n'avez pas bien nommé vos variables d'instance (attention à la convention des variables privées en python)."))

    def test_hier(self):
        for dates in DATES_INPUT:
            date_student = q.Date(
                dates["jour"], dates["mois"], dates["annee"])
            date_student.hier()

            date_corr = corr.Date(
                dates["jour"], dates["mois"], dates["annee"])
            date_corr.hier()

            message = "Pour la date {}/{}/{}, le résultat attendu est : {}/{}/{} mais votre code a produit {}/{}/{}".format(dates["jour"], dates["mois"], dates["annee"], date_corr.getJour(
            ), date_corr.getMois(), date_corr.getAnnee(), date_student.getJour(), date_student.getMois(), date_student.getAnnee())

            self.assertEqual(date_student.getJour(),
                             date_corr.getJour(), _(message))
            self.assertEqual(date_student.getMois(),
                             date_corr.getMois(), _(message))
            self.assertEqual(date_student.getAnnee(),
                             date_corr.getAnnee(), _(message))


if __name__ == '__main__':
    unittest.main()
