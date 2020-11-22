
import unittest

from Sieve import Sieve

class testsieve(unittest.TestCase):
    def testCalc(self):
        i=0
        for x in Sieve(16):
            i+=1
            if i==1:
                self.assertTrue(x==2)
            elif i==16:
                self.assertTrue(x==53)
            elif i>16:
                raise ValueError
if __name__ == "__main__":
    unittest.main()
