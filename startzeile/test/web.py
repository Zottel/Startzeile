import unittest

from startzeile.web import create_app

class WebTestCase(unittest.TestCase):

	def setUp(self):
		app = create_app(None, None)
		app.config['TESTING'] = True
		self.client = app.test_client()

	def tearDown(self):
		pass


class SimpleTestCase(WebTestCase):

	def test_basic_index(self):
		resp = self.client.get('/')
		print(resp.status_code)
		print(resp.headers)
		#print(resp.data)

	def test_basic_link(self):
		resp = self.client.get('/link/')
		print(resp.status_code)
		print(resp.headers)
		#print(resp.data)

	def test_basic_tag(self):
		resp = self.client.get('/tag/')
		print(resp.status_code)
		print(resp.headers)
		#print(resp.data)






def webSuite():
	suite = TestSuite()
	tests1 = unittest.TestLoader().loadTestsFromTestCase(WebTestCase)
	suite.addTests(tests1)
	tests2 = unittest.TestLoader().loadTestsFromTestCase(WebTestCase2)
	suite.addTests(tests2)
	return suite


