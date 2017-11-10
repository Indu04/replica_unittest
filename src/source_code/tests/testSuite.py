'''
Created on Sep 4, 2017

@author: jpi1
'''

import unittest
import testFactorial
import testPrime
# from testFactorial import testFactorial

loader = unittest.TestLoader()

suite = loader.loadTestsFromModule(testFactorial)
suite.addTests(loader.loadTestsFromModule(testPrime))


runner = unittest.TextTestRunner(verbosity=1)
result = runner.run(suite)
print result
