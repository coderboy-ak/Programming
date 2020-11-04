import unittest

class SignupTest(unittest.TestCase):
    def test_SignupbyEmail(self):
        print("This is Signup by email")
        self.assertTrue(True)

    def test_SignupbyFB(self):
        print("This is Signup by facebook")
        self.assertTrue(True)

    def test_SignupbyTWT(self):
        print("This is Signup by twitter")
        self.assertTrue(True)

if __name__=="__main__":
    unittest.main()