import unittest

from Seleniumpython.Package1.TC1_loginTest import LoginTest
from Seleniumpython.Package1.TC2_SignupTest import SignupTest
from Seleniumpython.Package2.TC3_PaymentTest import PaymentTest
from Seleniumpython.Package2.TC4_paymentReturns import PaymentReturnsTest

#Get all the tests from LoginTest,SignupTest,PaymentTest and PaymentReturnsTest
tc1= unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2= unittest.TestLoader().loadTestsFromTestCase(SignupTest)
tc3= unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
tc4= unittest.TestLoader().loadTestsFromTestCase(PaymentReturnsTest)

#Create test Suites
sanityTestSuite = unittest.TestSuite([tc1,tc2]) #SanityTestSuite
functionalTestSuite= unittest.TestSuite([tc3,tc4]) #FunctionalTestSuite
masterTestSuite= unittest.TestSuite([tc1,tc2,tc3,tc4]) #masterTestSuite

unittest.TextTestRunner(verbosity=2).run(masterTestSuite)

