#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random
import inspect
import sys

import CorrQ as corr
import df
import q

xsrp = lambda : random.randint(0, 5) #random positive, returns a extremly small random positive number.
srp = lambda : random.randint(0, 200) #random positive, returns a small random positive number.
rp = lambda : random.randint(0, sys.maxsize) #random positive, returns a random positive number.
lrp = lambda : random.randint(sys.maxsize/2, sys.maxsize) #large random positive, returns a big random positive number.


def rand_arg(r): #returns a dictionary {"a":_, "b":_, "nbPoints":_} such that b>a>=0, 200>nbPoints>=2, r is a function returning
        a = r()
        return {"a":a, "b":a+r(), "nbPoints":min(r(), 200)+2}

TESTS = [
            {
                "f": lambda x:0.0,
                "arg": {"a":0, "b":1, "nbPoints":2},
                "help": "You failed the integration of the null function "
            },
            {
                "f": lambda x:0,
                "arg": {"a":0, "b":0, "nbPoints":2},
                "help": "You failed the integration of the null function "
            },
            {
                "f": lambda x:0,
                "arg": rand_arg(xsrp),
                "help": "You failed the integration of the null function "
            },
            {
                "f": lambda x:0,
                "arg": rand_arg(srp),
                "help": "You failed the integration of the null function "
            },
            {
                "f": lambda x:x,
                "arg": {"a":0, "b":1, "nbPoints":2},
                "help": "You failed the integration of the identity function "
            },
            {
                "f": lambda x:x,
                "arg": {"a":0, "b":0, "nbPoints":2},
                "help": "You failed the integration of the identity function "
            },
            {
                "f": lambda x:x*x+x+1,
                "arg": rand_arg(xsrp),
                "help": "You failed the integration of the polynomial x² + x + 1 "
            },
            {
                "f": lambda x:x*x+x+1,
                "arg": rand_arg(lrp),
                "help": "You failed the integration of the polynomial x² + x + 1 for big numbers: check for overflows (sums of big numbers might exceed max float size!)."
            }
        ]

class TestExtractor(unittest.TestCase):
    def test_exist(self):
        self.assertTrue(dir(q)[-1] == dir(corr)[-1], "You did not name the method as expected.")

    def test_cases(self):
        for test in TESTS:
            print("Parameters " + str(test["arg"]))
            df.f = test["f"]
            correct_answer = corr.integrale(**test["arg"])
            student_answer = q.integrale(**test["arg"])
            self.assertEqual(correct_answer, student_answer, test["help"] + " for parameters " + str(test["arg"]) + ": expected " + str(correct_answer) + ", but you returned " + str(student_answer) + ".")


if __name__ == '__main__':
    unittest.main()
