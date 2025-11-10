import unittest
import math

szam1=int(input("Szam 1"))
szam2=int(input("Szam 2"))

def abs_max(a:int, b:int) -> int:
    if(abs(a)>abs(b)):
        return(abs(a))
    if(abs(a)<abs(b)):
        return(abs(b))

print(abs_max(szam1,szam2))


class Testek(unittest.TestCase):
    def test_nagyobb_nulla(self):
        nagyobb=int(abs_max(szam1,szam2))
        self.assertGreater(nagyobb,0)
        

unittest.main()