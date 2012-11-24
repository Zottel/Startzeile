import startzeile.test

import unittest

if __name__ == '__main__':
	testrunner = unittest.TextTestRunner(verbosity = 2)
	testsuite = startzeile.test.createSuite()
	testrunner.run(testsuite)

