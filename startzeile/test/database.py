import unittest

from startzeile.database import interface
from startzeile.database import dummy

class DBTestCase(unittest.TestCase):
	def __init__(self, database):
		super(DBTestCase, self).__init__()
		self.db = database
	
	def shortDescription(self):
		return 'Backend: %s' % self.db.shortDescription()
	
	def setUp(self):
		# Database has to be connected for our tests to work.
		if not self.db.connected():
			self.skipTest('not connected')
		pass
	
	def tearDown(self):
		pass

class ConnectedTest(DBTestCase):
	def runTest(self):
		self.assertTrue(self.db.connected())

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

class tagQueryTest(DBTestCase):
	def runTest(self):
		link = self.db.addLink(None, None, None, ['tagquery_a', 'tagquery_b', 'tagquery_c']);
		link2 = self.db.addLink(None, None, None, ['tagquery_a', 'tagquery_d']);
		link3 = self.db.addLink(None, None, None, ['tagquery_b', 'tagquery_e']);
		self.assertIn('tagquery_c', self.db.getTagsByTags(['tagquery_a', 'tagquery_b']));
		self.assertNotIn('tagquery_d', self.db.getTagsByTags(['tagquery_a', 'tagquery_b']));
		self.assertNotIn('tagquery_e', self.db.getTagsByTags(['tagquery_a', 'tagquery_b']));
		self.assertIn('tagquery_d', self.db.getTagsByTags(['tagquery_a']));

class deleteLinkTest(DBTestCase):
	def runTest(self):
		link = self.db.addLink(None, None, None, ['a', 'b', 'c'])
		link.delete()
		self.assertNotIn(link, self.db.getAllLinks())

		self.assertNotIn(link, self.db.getLinksByTags(['a']))
		self.assertNotIn(link, self.db.getLinksByTags(['b']))
		self.assertNotIn(link, self.db.getLinksByTags(['c']))
		
		with self.assertRaises(interface.LinkDeleted):
			link.getID()
		
		with self.assertRaises(interface.LinkDeleted):
			link.getTitle()
		
		with self.assertRaises(interface.LinkDeleted):
			link.setTitle(None)
		
		with self.assertRaises(interface.LinkDeleted):
			link.getURL()
		
		with self.assertRaises(interface.LinkDeleted):
			link.setURL(None)
		
		with self.assertRaises(interface.LinkDeleted):
			link.getDescription()
		
		with self.assertRaises(interface.LinkDeleted):
			link.setDescription(None)
		
		with self.assertRaises(interface.LinkDeleted):
			link.getTags()
		
		with self.assertRaises(interface.LinkDeleted):
			link.setTags(None)
		
		with self.assertRaises(interface.LinkDeleted):
			link.delete()

def createDBSuite(db):
	suite = unittest.TestSuite()
	tests = []
	tests.append(ConnectedTest(db))
	tests.append(AddLinkTest(db))
	tests.append(getAllLinksTest(db))
	tests.append(getLinksByTagsTest(db))
	tests.append(tagQueryTest(db))
	tests.append(changeTagsTest(db))
	tests.append(deleteLinkTest(db))
	suite.addTests(tests)
	return suite

def createSuite():
	suites = []
	suites.append(createDBSuite(dummy.Database()))
	return unittest.TestSuite(suites)
