"""
Flask Module Docs:  http://flask.pocoo.org/docs/api/#flask.Module

This file is used for both the routing and logic of your
application.
"""

from google.appengine.api import mail
from flask import Module, url_for, render_template, request, redirect, make_response
import simplejson as json 
views = Module(__name__, 'views')

@views.route('/')
def index():
    path = 'http://0.0.0.0:8080'
    static = 'http://0.0.0.0:8080/static'
    
    """Render website's index page."""
    return render_template('index.html', **locals())
    
@views.route('/docs/')
def docs():
    """Render documentation page."""
    return render_template('docs.html')
    
@views.route('/customize_library/')
def customize_library():
    path = 'http://0.0.0.0:8080'
    static = 'http://0.0.0.0:8080/static'
    
    # read tiramisu.json
    f = open('tiramisu.json', 'r')
    tiramisu_json = json.load(f)
    f.close()

    return render_template('customize_library.html', **locals())


@views.after_request
def add_header(response):
    """Add header to force latest IE rendering engine and Chrome Frame."""
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    return response


@views.app_errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
