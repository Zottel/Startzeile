from startzeile.database import interface

class Database(interface.Database):
	def __init__(self):
		self.links = {}
		self.tags = {}
		self.nextID = 0
		pass
	
	def shortDescription(self):
		return "dummy database"
	
	def connected(self):
		return True
	
	def getLink(self, link_id):
		if link_id in self.links:
			return self.links[link_id]
		else:
			raise interface.LinkNotFoundException()
	
	def getAllLinks(self):
		return self.links.values()
	
	def getLinksByTags(self, tags):
		result = None

		for tag in tags:
			if tag in self.tags:
				if result == None:
					result = self.tags[tag]
				else:
					result = result & self.tags[tag]
			else:
				return set()

		return result
	
	def getLinksByQuery(self):
		#TODO
		raise interface.NotImplementedException()
		pass
	
	def getTagsByTags(self, tags):
		#TODO
		raise interface.NotImplementedException()
		pass
	
	def getTagsByQuery(self, tags):
		#TODO
		raise interface.NotImplementedException()
		pass
	
	def addLink(self, title, url, description, tags):
		newID = self.nextID
		self.nextID = self.nextID + 1
		
		newLink = Link(self, newID)
		
		newLink.setTitle(title)
		newLink.setURL(url)
		newLink.setDescription(description)
		newLink.setTags(tags)
		
		self.links[newID] = newLink
		
		return newLink

class Link(interface.Link):
	def __init__(self, db, linkID):
		self.deleted = False
		self.db = db
		self.id = linkID
		self.title = None
		self.url = None
		self.description = None
		self.tags = set()
	
	def checkDeleted(f):
		def newF(self, *args, **kws):
			if self.deleted:
				raise interface.LinkDeletedException
			return f(self, *args, **kws)
		return newF
	
	@checkDeleted
	def getID(self):
		return self.id
	
	@checkDeleted
	def getTitle(self):
		return self.title
	
	@checkDeleted
	def setTitle(self, newTitle):
		self.title = newTitle
	
	@checkDeleted
	def getURL(self):
		return self.url
	
	@checkDeleted
	def setURL(self, newURL):
		self.url = newURL
	
	@checkDeleted
	def getDescription(self):
		return self.description
	
	@checkDeleted
	def setDescription(self, newDescription):
		self.description = newDescription
	
	@checkDeleted
	def getTags(self):
		return self.tags

	@checkDeleted
	def setTags(self, newTags):
		for tag in set(self.getTags()) - set(newTags):
			if tag in self.db.tags:
				self.db.tags[tag].remove(self)
		
		for tag in set(newTags) - set(self.getTags()):
			if not tag in self.db.tags:
				self.db.tags[tag] = set()
			self.db.tags[tag].add(self)
		
		self.tags = set(newTags)
	
	@checkDeleted
	def delete(self):
		self.deleted = True
		del self.db.links[self.id]
		for tag in self.tags:
			self.db.tags[tag].remove(self)

