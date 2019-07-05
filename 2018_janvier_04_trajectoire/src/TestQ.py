
#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import CorrQ as corr
import q

M=[
[0,0,0,0,0,1,0,0,0,0,1,0,0,1,0,0,1,0],
[0,0,1,1,0,0,0,0,0,1,0,1,0,0,0,0,1,0],
[0,0,1,1,1,0,0,1,1,0,0,0,1,1,1,0,0,0],
[0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,0,0],
[1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0],
[0,1,0,0,1,0,0,1,0,1,1,1,0,0,0,0,0,1],
[0,0,1,1,0,0,0,0,0,1,1,1,0,0,0,1,0,0]
]

M2 = [
[0,1,1,1,0,0,1,0],
[0,0,1,0,0,0,1,1],
[0,1,0,0,1,0,0,0],
[1,0,1,1,0,1,0,0],
[0,0,0,0,0,0,1,1],
]

M3 = [
    [0,0],
    [1,1]
]

class TestGetCountry(unittest.TestCase):
    def test_exist(self):
        self.assertTrue(hasattr(q, 'trajectoire'), _("You did not namee the method as expected."))

    def test_cases(self):
        corr_ans = corr.trajectoire(M)
        try_ans = q.trajectoire(M)
        corr_ans2 = corr.trajectoire(M2)
        try_ans2 = q.trajectoire(M2)
        corr_ans3 = corr.trajectoire(M3)
        try_ans3 = q.trajectoire(M3)

        self.assertTrue(corr_ans == try_ans, _("Vous ne retournez pas le bonne longueur"))
        self.assertTrue(corr_ans2 == try_ans2, _("Vous ne retournez pas le bonne longueur."))
        self.assertTrue(corr_ans3 == try_ans3, _("Vous ne retournez pas le bonne longueur."))

if __name__ == '__main__':
    unittest.main()