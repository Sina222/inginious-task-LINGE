#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

import unittest
import random
import math
import array

import CorrQ as corr
import q

# creating a random hight
n = random.randint(2,10)

original = sys.stdout
b = bytearray()

class TestExtractor(unittest.TestCase):
    def test_exist(self):
        self.assertTrue(hasattr(q, 'triangle3'), _("You did not name the method as expected."))

    def test_cases(self):
        # test random
        stu_ans = open("stu_ans.txt", 'w')
        sys.stdout = stu_ans
        q.triangle3(n)
        stu_ans.close()
        corr_ans = open("corr_ans.txt", 'w')
        sys.stdout = corr_ans
        corr.triangle3(n)
        corr_ans.close()
        corr_ans = open("corr_ans.txt", 'r')
        correct = corr_ans.read()
        stu_ans = open("stu_ans.txt", 'r')
        stud = stu_ans.read()
        self.assertEqual(correct, stud,_("Your triangle is not the one expected : \n The correct triangle with his corresponding bytes array : {} \n {} \n Your triangle with his corresponding bytes array : {} \n {} \n .").format(correct,[ord(c) for c in correct],stud,[ord(c) for c in stud]))
        corr_ans.close()
        stu_ans.close()

        # test with hight == 1
        stu_ans = open("stu_ans.txt", 'w')
        sys.stdout = stu_ans
        q.triangle3(1)
        stu_ans.close()
        corr_ans = open("corr_ans.txt", 'w')
        sys.stdout = corr_ans
        corr.triangle3(1)
        corr_ans.close()
        corr_ans = open("corr_ans.txt", 'r')
        correct = corr_ans.read()
        stu_ans = open("stu_ans.txt", 'r')
        stud = stu_ans.read()
        self.assertEqual(correct, stud,_("Your methode did not print a correct triangle with hight 1."))
        corr_ans.close()
        stu_ans.close()

        #test with hight == 0
        stu_ans = open("stu_ans.txt", 'w')
        sys.stdout = stu_ans
        q.triangle3(0)
        stu_ans.close()
        corr_ans = open("corr_ans.txt", 'w')
        sys.stdout = corr_ans
        corr.triangle3(0)
        corr_ans.close()
        corr_ans = open("corr_ans.txt", 'r')
        correct = corr_ans.read()
        stu_ans = open("stu_ans.txt", 'r')
        stud = stu_ans.read()
        self.assertEqual(correct, stud,_("Your methode did not print the right result for a 0 hight triangle"))
        corr_ans.close()
        stu_ans.close()
        sys.stdout = original

if __name__ == '__main__':
    unittest.main()
