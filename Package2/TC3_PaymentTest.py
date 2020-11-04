import unittest

class PaymentTest(unittest.TestCase):
    def test_Paymentdollar(self):
        print("This is payment in dollar test")
        self.assertTrue(True)

    def test_Paymentrupees(self):
        print("This is payment in rupees test")
        self.assertTrue(True)

if __name__=="__main__":
    unittest.main()