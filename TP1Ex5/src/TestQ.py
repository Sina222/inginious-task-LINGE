#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import q
import CorrQ as corr
import random
import string

#set of string
string_set = ["Kerys Andersen",
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

#Creation of the random string s
s = random.choice(string_set)
s_random = (s,_(" You did not reverse the string : {} \n Your result : {} \n Expected result : {}"))
s_empty = ("",_("You did not pass the test for an empty string, you should return the empty string."))
s_one = (random.choice(string.ascii_lowercase),_("You did not pass the test for one letter : {}. \n Your result : {} \n Expected result : {}"))

TEST = [s_random,s_empty,s_one]


class TestPageRank(unittest.TestCase):

	def test_exist_name(self):
		self.assertTrue(hasattr(q, 'mirroir'), _("You did not name the method as expected."))

	def test(self):
		for test in TEST :
			stud_ans = q.mirroir(test[0])
			corr_ans = corr.mirroir(test[0])
			self.assertEqual(stud_ans,corr_ans,test[1].format(test[0],stud_ans,corr_ans))

if __name__ == '__main__':
	unittest.main()
