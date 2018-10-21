from flask import Flask, render_template, json, url_for
from pprint import pprint
import os
import json

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html', active='index')

@app.route('/habitat')
def habitat():
	SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
	with open(os.path.join(SITE_ROOT,'static', 'data.json')) as f:
		data = json.load (f)
        	return render_template('habitat.html', active='habitat')

@app.route('/reptiles')
def reptiles():
	SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
	with open(os.path.join(SITE_ROOT,'static', 'data.json')) as f:
		data = json.load (f)
		return render_template ('reptiles.html', active='reptiles',  data=data)


@app.route('/mammals')	
def mammals():
	SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
	with open (os.path.join(SITE_ROOT, 'static', 'data.json')) as f:
		data = json.load (f)
		return render_template ('mammals.html', active='mammals', data=data)


@app.route('/birds')
def birds():
	SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
	with open (os.path.join(SITE_ROOT, 'static', 'data.json')) as f:
		data = json.load (f)
		return render_template ('birds.html', active='birds', data=data)

@app.route('/amphibian')
def amphibian():
	SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
	with open (os.path.join(SITE_ROOT, 'static', 'data.json')) as f:
		data = json.load (f)
		return render_template ('amphibian.html', active='amphibian', data=data)

@app.errorhandler(404)
def not_found_error(error)
	return render_template('404.html'), 404
