# -*- coding: utf-8
from flask.views import View, MethodView
from flask import request, session, g, redirect, render_template, flash


class RESTLink(MethodView):

	def get(self, filetype, link_id = None):
		return render_template('link.xhtml')
		# TODO: return the requested link
		pass

	def post(self, filetype):
		# TODO: Create link
		pass

	def delete(self, filetype, link_id):
		# TODO: Delete Link
		pass

	def put(self, filetype, link_id):
		# TODO: Update Link
		pass

	def __init__(self, startzeile):
		self.startzeile = startzeile
		pass

