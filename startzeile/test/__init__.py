__all__ = ['web']

import unittest
import startzeile.test.web

def createSuite():
	suites = []
	suites.append(startzeile.test.web.createSuite())
	suite = unittest.TestSuite(suites)
	return suite

