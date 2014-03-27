
class Database():
	def __init__(self):
		pass
	
	def shortDescription(self):
		return "Database Interface"
	
	def connected(self):
		pass
	
	def getLink(self, link_id):
		pass
	
	def getAllLinks(self):
		pass
	
	def getLinksByTags(self, tags):
		pass
	
	def getLinksByQuery(self, query):
		pass
	
	def getTagsByTags(self, tags):
		pass
	
	def getTagsByQuery(self, query):
		pass
	
	def addLink(self, title, url, description, tags):
		pass
	
	def getUser(self):
		pass
	
	def getGroup(self):
		pass

class User():
	def getName(self):
		pass
	
	def validatePassword(self, password):
		pass
	
	def hasPermission(self, name):
		pass
	
	def getGroups(self):
		pass

class Group():
	pass

class Link():
	def __init__(self, db):
		self.db = db
	
	def getID(self):
		pass
	
	def getTitle(self):
		pass
	
	def setTitle(self, newTitle):
		pass
	
	def getOwner(self):
		pass
	
	def getURL(self):
		pass
	
	def setURL(self, newURL):
		pass
	
	def getDescription(self):
		pass
	
	def setDescription(self, newDescription):
		pass
	
	def getTags(self, tags):
		pass
	
	def setTags(self, newTags, oldTags = []):
		pass
	
	def delete(self):
		pass

class LinkNotFound(Exception):
	pass

class LinkDeleted(Exception):
	pass

class NotImplemented(Exception):
	pass
