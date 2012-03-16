# -*- coding: utf-8
from flask.views import View, MethodView
from flask import request, session, g, redirect, render_template, flash


class RESTLink(MethodView):

	def get(self, type, link_id = None):
		if link_id is None:
			return render_template('link.xhtml')
			# TODO: Decide what to do here…
			pass
		else:
			return render_template('link.xhtml')
			# TODO: return the requested link
			pass

	def post(self):
		# TODO: Create link
		pass

	def delete(self, link_id):
		# TODO: Delete Link
		pass

	def put(self, link_id):
		# TODO: Update Link
		pass

	def __init__(self, startzeile):
		self.startzeile = startzeile
		pass

