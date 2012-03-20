import unittest

import startzeile.database.dummy

class DBTestCase(unittest.TestCase):
	def setUp(self):
		self.db = startzeile.database.dummy.Database()
		pass

	def tearDown(self):
		pass

class AddLinkTest(DBTestCase):
	def runTest(self):
		link = self.db.addLink('testtitle', 'testurl', 'testdesc', ['a', 'b', 'c'])
		self.assertEqual(link, self.db.getLink(link.getID()))
		self.assertEqual(link.getTitle(), 'testtitle')
		self.assertEqual(link.getURL(), 'testurl')
		self.assertEqual(link.getDescription(), 'testdesc')
		self.assertEqual(link.getTags(), ['a', 'b', 'c'])
		self.assertIn(link, self.db.getAllLinks())
		self.assertIn(link, self.db.getLinksByTags(['a', 'c']))
		self.assertIn(link, self.db.getLinksByTags(['b']))
		self.assertIn(link, self.db.getLinksByTags(['a', 'b', 'c']))

class getAllLinksTest(DBTestCase):
	def runTest(self):
		for link in self.db.getAllLinks():
			self.assertIsInstance(link, startzeile.database.interface.Link)

class getLinksByTags(DBTestCase):
	def runTest(self):
		abc = self.db.addLink(None, None, None, ['a', 'b', 'c'])
		a = self.db.addLink(None, None, None, ['a'])
		bc = self.db.addLink(None, None, None, ['b', 'c'])
		ab = self.db.addLink(None, None, None, ['a', 'b'])
		self.assertIn(abc, self.db.getLinksByTags(['a']))
		self.assertIn(a, self.db.getLinksByTags(['a']))
		self.assertIn(ab, self.db.getLinksByTags(['a']))
		self.assertNotIn(a, self.db.getLinksByTags(['b']))
		self.assertNotIn(bc, self.db.getLinksByTags(['a']))

def createSuite():
	suite = unittest.TestSuite()
	tests = []
	tests.append(AddLinkTest())
	tests.append(getAllLinksTest())
	tests.append(getLinksByTags())
	suite.addTests(tests)
	return suite
