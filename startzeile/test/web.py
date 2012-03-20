import unittest

from startzeile.web import create_app


class WebTestCase(unittest.TestCase):

	def setUp(self):
		app = create_app(None, None)
		app.config['TESTING'] = True
		self.client = app.test_client()

	def tearDown(self):
		pass


class BasicDefaultTestCase(WebTestCase):
	def runTest(self):
		resp = self.client.get('/')
		self.assertEqual(resp.status_code, 200)
		#print(resp.status_code)
		#print(resp.headers)
		#print(resp.data)

class BasicLinkTestCase(WebTestCase):
	def runTest(self):
		resp = self.client.get('/link/%d.html' % 0)
		self.assertEqual(resp.status_code, 200)
		#print(resp.status_code)
		#print(resp.headers)
		#print(resp.data)

class BasicQueryTestCase(WebTestCase):
	def runTest(self):
		resp = self.client.get('/query/all.html')
		self.assertEqual(resp.status_code, 200)
		#print(resp.status_code)
		#print(resp.headers)
		#print(resp.data)

class BasicTagsTestCase(WebTestCase):
	def runTest(self):
		resp = self.client.get('/tags/test.html')
		self.assertEqual(resp.status_code, 200)
		#print(resp.status_code)
		#print(resp.headers)
		#print(resp.data)

def createSuite():
	suite = unittest.TestSuite()
	tests = []
	tests.append(BasicDefaultTestCase())
	tests.append(BasicLinkTestCase())
	tests.append(BasicQueryTestCase())
	tests.append(BasicTagsTestCase())
	suite.addTests(tests)
	return suite


