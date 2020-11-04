import unittest
def setUpModule(): #execute before class starts
    print("setUpModule")
def tearDownModule(): #execute after class ends
    print("tearDownModule")
class AppTesting(unittest.TestCase):

    @classmethod
    def setUp(self):
        print("setUp : This will execute before every method")

    @classmethod
    def tearDown(self):
        print("tearDown : This will execute after every test method")

    @classmethod
    def setUpClass(cls):
        print("Open application : setUpClass -  Execute once before all test methods")

    @classmethod
    def tearDownClass(cls):
        print("Close application : tearDownClass - Execute once after all test methods")

    @unittest.SkipTest
    def test_search(self):
        print("This is search test")

    @unittest.skip("Skipping this method bcoz it is not ready")
    def test_prepaidRecharge(self):
        print("This is prepaid recharge test")

    @unittest.skipIf(1==1,"Numbers should not be equal")
    def test_postpaidRecharge(self):
        print("This is prepaid recharge test")

    def test_Recharge(self):
        print("This is recharge test")

if __name__=="__main__":
    unittest.main()

# setupmodule - execute before class only once
# setupclass- execute once before all methods
# setup-execute multiple times before every method
# method function
# teardown-execute multiple times after every methods
# teardownclass- execute once after all methods
# teardownmodule- execute only once after class/module completion

# skipping test 3 types:
# @unittest.SkipTest
# @unittest.skip("give reason of skipping test")
# @unittest.skipIf(1==1,"Give condition for skipping")