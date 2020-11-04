import unittest

#To use the method present in UnitTesting framework ,we have to extend the TestCase class present in Unittest module
class Test(unittest.TestCase):
    def test_FirstTest(self): #every method of each test case should began with test_name
        print("This is my first unit test case")

if __name__=="__main__":
    unittest.main()