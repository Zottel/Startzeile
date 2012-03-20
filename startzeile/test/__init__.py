__all__ = ['web']

import unittest
import startzeile.test.web
import startzeile.test.database

def createSuite():
	suites = []
	suites.append(startzeile.test.web.createSuite())
	suites.append(startzeile.test.database.createSuite())
	suite = unittest.TestSuite(suites)
	return suite

