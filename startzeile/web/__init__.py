# Flask
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

# Web interface components
import link, query, tag

def create_app(startzeile, config):
	app = Flask(__name__)
	app.config.from_object(config)
	
	# Default page - only needed when visited by user => only html
	@app.route('/')
	@app.route('/index.html')
	def show_default():
		return render_template('index.xhtml')
	
	# Link view + url handling
	link_view = link.RESTLink.as_view('link_api', startzeile)
	
	app.add_url_rule('/link.<filetype>',
	                 view_func=link_view,
	                 methods=['POST'])
	
	app.add_url_rule('/link/<int:link_id>.<filetype>',
	                 view_func=link_view,
	                 methods=['GET', 'PUT', 'DELETE'])
	
	# Query view + url handling
	query_view = query.QueryView.as_view('query_api', startzeile)
	
	app.add_url_rule('/query.<filetype>',
	                 view_func=query_view,
									 defaults = {'querytype': 'post'},
	                 methods=['POST'])
	
	app.add_url_rule('/query/all.<filetype>',
	                 view_func=query_view,
									 defaults = {'querytype': 'all'},
	                 methods=['GET'])
	
	app.add_url_rule('/query/tags/<path:tags>.<filetype>',
	                 view_func=query_view,
									 defaults = {'querytype': 'tags'},
	                 methods=['GET'])
	
	# Tag view + url handling
	tag_view = tag.TagView.as_view('tag_api', startzeile)
	
	app.add_url_rule('/tags.<filetype>',
	                 view_func=tag_view,
	                 methods=['GET'])
	
	app.add_url_rule('/tags/<path:tags>.<filetype>',
	                 view_func=tag_view,
	                 methods=['GET'])
	
	return app

# Submodules
__all__ = ['views']

