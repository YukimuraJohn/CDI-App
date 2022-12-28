## This Files is used to make some tests

import unittest
import decimal
import cdi
from cdi import BFunc

class TestBasicFunctions(unittest.TestCase):
    # Function test_jc is going to call function jc() using parameters:
    # self, r = 1, t = 2 and n = 1, and that returns 3.0 as result.
    def test_jc(self):
        self.jc = BFunc.jc(self,1,2,1)
        self.jc = decimal.Decimal(self.jc)
        self.assertEqual(float(round(self.jc, 2)), 3.0)
    
    # Function test_year2day is going to call function year2day() using parameters:
    # self and a = 2, and that returns rounded 0.44
    def test_year2day(self):
        self.y2d = decimal.Decimal(BFunc.year2day(self,2))
        #self.y2d = decimal.Decimal(self.y2d)
        self.assertEqual(float(round(self.y2d, 2)), 0.44)

    # Function test_year2month is going to call function year2month() using parameters:
    # self and a = 2, and that returns rounded 9.59
    def test_year2month(self):
        self.y2m = decimal.Decimal(BFunc.year2month(self,2))
        self.assertEqual(float(round(self.y2m, 2)), 9.59)

    # Function test_doublePrincipal is going to call function doublePrincipal() using
    # parameters: self and r = 2, and that returns rounded 0.63
    def test_doublePrincipal(self):
        #txPoupM = self.test_year2month(self.txPoup/100.0)
        self.doubP = decimal.Decimal(BFunc.doublePrincipal(self,2))
        self.assertEqual(float(round(self.doubP, 2)), 0.63)

    # Function test_checkAmountSavings is checking the result with 13.25 and 
    # 8.5 for selic values, returning respectively the values 6.17 and
    # 5.95
    def test_checkAmountSavings(self):
        self.chASYear = decimal.Decimal(BFunc.checkAmountSavings(self,13.25))
        self.assertEqual(float(round(self.chASYear, 2)), 6.17)
        self.chASYear2 = decimal.Decimal(BFunc.checkAmountSavings(self, 8.5))
        self.assertEqual(float(round(self.chASYear2, 2)), 5.95)
    
    # Conflicting with something else, repair after --> :to do:
    # def test_CDB(self):
    #     self.CDB = decimal.Decimal(BFunc.CDB(self, 1000, 0.1315, 93.0, 6.17, 22.5, 1))
    #     self.assertEqual(float(round(self.CDB, 2)), 0)
    
    # Function test_TransPorc is going to test transPort(), that return the percentage value
    def test_TransPorc(self):
        self.assertEqual(BFunc.transPorc(self, 0.12), 12.0)
    
    # Function test_Usage checks if str(cdi.usage()) is instance str
    def test_Usage(self):
        self.assertIsInstance(str(cdi.usage()), str)

if __name__ == '__main__':
    unittest.main()