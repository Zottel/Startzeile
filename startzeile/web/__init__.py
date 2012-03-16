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
		return render_template('default.xhtml')

	# Link view + url handling
	link_view = link.RESTLink.as_view('link_api', startzeile)
	
	app.add_url_rule('/link.<type>',
	                 view_func=link_view,
	                 methods=['POST'])
	
	app.add_url_rule('/link/<int:link_id>.<type>',
	                 view_func=link_view,
	                 methods=['GET', 'PUT', 'DELETE'])

	# Query view + url handling
	query_view = query.QueryView.as_view('query_api', startzeile)
	
	app.add_url_rule('/query.<type>',
	                 view_func=query_view,
	                 methods=['POST'])
	
	app.add_url_rule('/query/all.<type>',
	                 view_func=query_view,
	                 methods=['GET'])

	app.add_url_rule('/query/tags/<path:tags>.<type>',
	                 view_func=query_view,
	                 methods=['GET'])

	# Tag view + url handling
	tag_view = tag.TagView.as_view('tag_api', startzeile)
	
	app.add_url_rule('/tags.<type>',
	                 view_func=tag_view,
	                 methods=['GET'])
	
	app.add_url_rule('/tags/<path:tags>.<type>',
	                 view_func=tag_view,
	                 methods=['GET'])
	
	return app

# Submodules
__all__ = ['views']

