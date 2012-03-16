# Flask
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

# Web interface components
from views import *

def create_app(startzeile, config):
	app = Flask(__name__)
	app.config.from_object(config)

	link_view = RESTLink.as_view('link_api', startzeile)

	app.add_url_rule('/link/', defaults={'link_id': None},
	                 view_func=link_view, methods=['GET',])

	app.add_url_rule('/link/', view_func=link_view, methods=['POST',])
	app.add_url_rule('/link/<int:link_id>', view_func=link_view,
	                 methods=['GET', 'PUT', 'DELETE'])

	return app

__all__ = ['views']

