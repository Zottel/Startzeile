
class Database():
	def __init__(config):
		pass
	
	def getLink(link_id):
		pass
	
	def getAllLinks():
		pass
	
	def getLinksByTags(tags):
		pass
	
	def getLinksByQuery():
		pass
	
	def getTagsByTags(tags):
		pass
	
	def getTagsByQuery(tags):
		pass

class Link():
	def __init__(self, db):
		self.db = db
	
	def getTitle():
		pass
	
	def getID():
		pass
	
	def getURL():
		pass
	
	def getDescription():
		pass

class Tag():
	def __init__(self, db):
		self.db = db
	
	def getName():
		pass
	
	def getLinks():
		pass

