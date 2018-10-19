from flask import Flask, render_template, json, url_for
from pprint import pprint
import os
import json




app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/habitat')
def habitat():
	SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
	with open(os.path.join(SITE_ROOT,'static', 'data.json')) as f:
		data = json.load (f)
        	return render_template('habitat.html')

@app.route('/reptiles')
def reptiles():
	SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
	with open(os.path.join(SITE_ROOT,'static', 'data.json')) as f:
		data = json.load (f)
		return render_template ('reptiles.html', data=data)


@app.route('/mammals')	
def mammals():
	SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
	with open (os.path.join(SITE_ROOT, 'static', 'data.json')) as f:
		data = json.load (f)
		return render_template ('mammals.html', data=data)


@app.route('/birds')
def birds():
	SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
	with open (os.path.join(SITE_ROOT, 'static', 'data.json')) as f:
		data = json.load (f)
		return render_template ('birds.html', data=data)

@app.route('/amphibian')
def amphibian():
	SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
	with open (os.path.join(SITE_ROOT, 'static', 'data.json')) as f:
		data = json.load (f)
		return render_template ('amphibian.html', data=data)

