from flask.views import MethodView
from flask import request, session, g, redirect, render_template, flash

class RESTLink(MethodView):

	def get(self, link_id):
		if link_id is None:
			# return a list of users
			pass
		else:
			# expose a single user
			pass

	def post(self):
		# create a new user
		pass

	def delete(self, link_id):
		# delete a single user
		pass

	def put(self, link_id):
		# update a single user
		pass

	def __init__(self, startzeile):
		self.startzeile = startzeile
		pass

class RESTQuery(MethodView):
	pass

class RESTTag(MethodView):
	pass


