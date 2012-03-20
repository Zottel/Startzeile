# -*- coding: utf-8
from flask.views import View, MethodView
from flask import request, session, g, redirect, render_template, flash


class TagView(View):
	methods = ['GET', 'POST']

	def __init__(self, startzeile):
		self.startzeile = startzeile
	pass
	
	def dispatch_request(self, filetype, tags = ''):
		return render_template('default.xhtml')
		pass
	
