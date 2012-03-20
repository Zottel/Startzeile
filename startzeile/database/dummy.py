import startzeile.database.interface

class Database(startzeile.database.interface.Database):
	def __init__(self):
		self.links = {}
		self.tags = {}
		self.nextID = 0
		pass
	
	def getLink(self, link_id):
		if link_id in self.links:
			return self.links[link_id]
		else:
			raise startzeile.database.interface.LinkNotFoundException()
	
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
		pass
	
	def getTagsByTags(self, tags):
		#TODO
		pass
	
	def getTagsByQuery(self, tags):
		#TODO
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

class Link(startzeile.database.interface.Link):
	def __init__(self, db, linkID):
		self.deleted = False
		self.db = db
		self.id = linkID
		self.title = None
		self.url = None
		self.description = None
		self.tags = set()
	
	def getID(self):
		if self.deleted:
			raise startzeile.database.interface.LinkDeletedException
		return self.id
	
	def getTitle(self):
		if self.deleted:
			raise startzeile.database.interface.LinkDeletedException
		return self.title
	
	def setTitle(self, newTitle):
		if self.deleted:
			raise startzeile.database.interface.LinkDeletedException
		self.title = newTitle
	
	def getURL(self):
		if self.deleted:
			raise startzeile.database.interface.LinkDeletedException
		return self.url
	
	def setURL(self, newURL):
		if self.deleted:
			raise startzeile.database.interface.LinkDeletedException
		self.url = newURL
	
	def getDescription(self):
		if self.deleted:
			raise startzeile.database.interface.LinkDeletedException
		return self.description
	
	def setDescription(self, newDescription):
		if self.deleted:
			raise startzeile.database.interface.LinkDeletedException
		self.description = newDescription
	
	def getTags(self):
		if self.deleted:
			raise startzeile.database.interface.LinkDeletedException
		return self.tags
	
	def setTags(self, newTags, oldTags = []):
		if self.deleted:
			raise startzeile.database.interface.LinkDeletedException
		for tag in newTags:
			if not tag in self.db.tags:
				self.db.tags[tag] = set()
			self.db.tags[tag].add(self)
		# TODO: remove from old tags
		
		self.tags = newTags
	
	def delete():
		self.deleted = True
		del self.db.links[self.id]
		for tag in self.tags:
			self.db.tags[tag].remove(self)

