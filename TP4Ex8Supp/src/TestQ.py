#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

import unittest
import random
import math
from unittest.mock import patch

import CorrQ as corr
import q

# set of names
names_set = ["Kerys Andersen",
"Faheem Dickerson",
"Amaan Forrest",
"Arvin Wardle",
"Shanna Brown",
"Ayyub Witt",
"Rodrigo Haas",
"Georgia Jackson",
"Ehsan Rivas",
"Habib Mccormack",
"Rianna Monroe",
"Felix Novak",
"Zayaan Bloom",
"Kanye Davila",
"Curtis Hardin",
"Tala Burt",
"Cataleya Lyon",
"Harlan Hutchings",
"Alma Stubbs",
"Alysia Woodard",
"Tamika Butt",
"Adeline Goff",
"Imaan Armitage",
"Ruby-May Woodley",
"Alisa Rice",
"Lucie Kearney",
"Alana Reese",
"T-Jay Broadhurst",
"Pearl Mcfarland",
"Korey Bridges",
"Nora Kirby",
"Mahamed Glass",
"Zachariah Fraser",
"Tristan Knight",
"Jez Powell",
"Samera Forbes",
"Kier Orozco",
"Ezmae Short",
"Sherry Mccabe",
"Aras Haworth",
"Monique Flowers",
"Ava-Mai Gill",
"Ceara Higgs",
"Desiree Garcia",
"Arabella Bannister",
"Caine Burks",
"Sania Hastings",
"Yu Fisher",
"Zayne Shaffer",
"Cheyenne O'Gallagher"]

#selecting names among the names set
nb_names = random.randint(5,10)
names = [(names_set[i],random.randint(0,nb_names-i)) for i in range(nb_names)]

original = sys.stdout
b = bytearray()

def stdin_test():
    to_ret = []
    n_last = 5
    #insert all the names
    for (name,n) in names:
        to_ret.append(name)

    #pass to the other loop
    to_ret.append("")

    #try to delete a non existing name
    to_ret.append(str(len(names)))

    #remove all the names
    for (name,n) in names :
        n_last = n
        to_ret.append(n)

    #try to remove when empty
    to_ret.append(n_last)

    #exit the second loop
    to_ret.append(-1)

    return to_ret

class TestExtractor(unittest.TestCase):
    def test_exist(self):
        self.assertTrue(hasattr(q, 'main'), _("You did not name the method as expected."))

    def test_cases(self):
        # test random
        stu_ans = open("stu_ans.txt", 'w')
        sys.stdout = stu_ans
        user_input = stdin_test()
        with patch('builtins.input', side_effect=user_input):
            q.main()
        stu_ans.close()
        corr_ans = open("corr_ans.txt", 'w')
        sys.stdout = corr_ans
        with patch('builtins.input', side_effect=user_input):
            corr.main()
        corr_ans.close()
        corr_ans = open("corr_ans.txt", 'r')
        correct = corr_ans.read()
        stu_ans = open("stu_ans.txt", 'r')
        stud = stu_ans.read()
        self.assertEqual(correct, stud,_("Your output don't match the expected one. \n The expected one:\n {} \n Your output:\n {}\n The input : \n {} ").format(correct,stud,user_input))
        corr_ans.close()
        stu_ans.close()


if __name__ == '__main__':
    unittest.main()
