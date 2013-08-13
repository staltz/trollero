
from flask import render_template, request
from app import app
from app.logic import generate_text

@app.route('/')
def index():
	context = {
		'troll_text': generate_text(),
	}
	return render_template('index.html', **context)

@app.route('/_get_text')
def get_troll_text():
	return generate_text(request.args.get('subject'))
