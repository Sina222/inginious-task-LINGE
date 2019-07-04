#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import random

import CorrQ as corr
import q


INPUTS = [
    {
        "table": [3, 6, 7, 10, 13, 11, 11, 12, 10, 9, 7, 5, 4, 3, 3, 4, 3, 4, 2, 1, 2],
        "interval": [
            [4, 7], [0, 20], [7, 17], [0, 1], [4, 15]
        ]
    },
    {
        "table": [1, 2],
        "interval": [
            [0, 1]
        ]
    },
    {
        "table": [42, 42, 42, 42, 42, 42, 42, 42, 42, 42],
        "interval": [
            [3, 8], [0, 9]
        ]
    },
    {
        "table": [-36, -25, -16, -9, -4, -1, 0, -1, -4, -9, -16, -25, -36],
        "interval": [
            [3, 8], [0, 10], [0, 12]
        ]
    },
    {
        "table": [36, 25, 16, 9, 4, 1, 0, 1, 4, 9, 16, 25, 36],
        "interval": [
            [3, 8], [0, 10], [0, 12]
        ]
    }
]


class TestValee(unittest.TestCase):

    def test_specs_q1(self):
        self.assertTrue(hasattr(q, 'maximaLocaux') and callable(
            q.maximaLocaux), "@1@: " + _("Vous n'avez pas bien spécifié votre fonction."))

    def test_specs_q2(self):
        self.assertTrue(hasattr(q, 'estVallee') and callable(
            q.estVallee), "@2@: " + _("Vous n'avez pas bien spécifié votre fonction."))

    def test_specs_q3(self):
        self.assertTrue(hasattr(q, 'plusGrandeVallee') and callable(
            q.plusGrandeVallee), "@3@: " + _("Vous n'avez pas bien spécifié votre fonction."))

    def test_q1(self):
        sol = corr.EXAM_JAN2018_Q3()
        for i in INPUTS:
            try:
                student_q1 = q.maximaLocaux(i["table"])
            except Exception as e:
                self.fail("@1@: " + str(e))

            sol_q1 = sol.maximaLocaux(i["table"])

            self.assertEqual(student_q1, sol_q1, "@1@: " + _(
                "Pour le tableau : {}\nvotre code a produit : {}\nmais le résulat attendu est : {}".format(i["table"], student_q1, sol_q1)))

    def test_q2(self):
        sol = corr.EXAM_JAN2018_Q3()
        for i in INPUTS:
            for interval in i["interval"]:
                try:
                    student_q2 = q.estVallee(
                        i["table"], interval[0], interval[1])
                except Exception as e:
                    self.fail("@2@: " + str(e))

                sol_q2 = sol.estVallee(i["table"], interval[0], interval[1])

                self.assertEqual(student_q2, sol_q2, "@2@: " + _(
                    "Pour le tableau : {}\net a={}, b={}\nvotre code a produit : {}\nmais le résulat attendu est : {}".format(i["table"], interval[0], interval[1], student_q2, sol_q2)))

    def test_q3(self):
        sol = corr.EXAM_JAN2018_Q3()
        for i in INPUTS:
            try:
                student_q3 = q.plusGrandeVallee(i["table"])
            except Exception as e:
                self.fail("@3@: " + str(e))

            sol_q3 = sol.plusGrandeVallee(i["table"])

            self.assertEqual(student_q3, sol_q3, "@3@: " + _(
                "Pour le tableau : {}\nvotre code a produit : {}\nmais le résulat attendu est : {}".format(i["table"], student_q3, sol_q3)))


if __name__ == '__main__':
    unittest.main()
