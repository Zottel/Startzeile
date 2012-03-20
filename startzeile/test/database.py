import unittest

from startzeile.database import interface
from startzeile.database import dummy

class DBTestCase(unittest.TestCase):
	def setUp(self):
		self.db = dummy.Database()
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
		self.assertEqual(link.getTags(), {'a', 'b', 'c'})
		self.assertIn(link, self.db.getAllLinks())
		self.assertIn(link, self.db.getLinksByTags(['a', 'c']))
		self.assertIn(link, self.db.getLinksByTags(['b']))
		self.assertIn(link, self.db.getLinksByTags(['a', 'b', 'c']))

class getAllLinksTest(DBTestCase):
	def runTest(self):
		for link in self.db.getAllLinks():
			self.assertIsInstance(link, interface.Link)

class getLinksByTagsTest(DBTestCase):
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

class changeTagsTest(DBTestCase):
	def runTest(self):
		link = self.db.addLink(None, None, None, ['a', 'b'])
		self.assertIn(link, self.db.getLinksByTags(['a']))
		self.assertIn(link, self.db.getLinksByTags(['b']))
		link.setTags(['a'])
		self.assertEqual({'a'}, link.getTags())
		self.assertIn(link, self.db.getLinksByTags(['a']))
		self.assertNotIn(link, self.db.getLinksByTags(['b']))
		link.setTags(['b'])
		self.assertEqual({'b'}, link.getTags())
		self.assertIn(link, self.db.getLinksByTags(['b']))
		self.assertNotIn(link, self.db.getLinksByTags(['a']))

class deleteLinkTest(DBTestCase):
	def runTest(self):
		link = self.db.addLink(None, None, None, ['a', 'b', 'c'])
		link.delete()
		self.assertNotIn(link, self.db.getLinksByTags(['a']))
		self.assertNotIn(link, self.db.getLinksByTags(['b']))
		self.assertNotIn(link, self.db.getLinksByTags(['c']))
		
		with self.assertRaises(interface.LinkDeletedException) as cm:
			link.getID()
		
		with self.assertRaises(interface.LinkDeletedException) as cm:
			link.getTitle()
		
		with self.assertRaises(interface.LinkDeletedException) as cm:
			link.setTitle(None)
		
		with self.assertRaises(interface.LinkDeletedException) as cm:
			link.getURL()
		
		with self.assertRaises(interface.LinkDeletedException) as cm:
			link.setURL(None)
		
		with self.assertRaises(interface.LinkDeletedException) as cm:
			link.getDescription()
		
		with self.assertRaises(interface.LinkDeletedException) as cm:
			link.setDescription(None)
		
		with self.assertRaises(interface.LinkDeletedException) as cm:
			link.getTags()
		
		with self.assertRaises(interface.LinkDeletedException) as cm:
			link.setTags(None)
		
		with self.assertRaises(interface.LinkDeletedException) as cm:
			link.delete()

def createSuite():
	suite = unittest.TestSuite()
	tests = []
	tests.append(AddLinkTest())
	tests.append(getAllLinksTest())
	tests.append(getLinksByTagsTest())
	tests.append(changeTagsTest())
	tests.append(deleteLinkTest())
	suite.addTests(tests)
	return suite
